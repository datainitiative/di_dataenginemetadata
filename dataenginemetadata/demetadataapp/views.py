from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db import models
from django.db.models.loading import get_model
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm

# Import from general utilities
from demetadataapp.util import *
# Import from app
from dataenginemetadata.settings import ADMIN_ROOT_URL, ROOT_APP_URL, STATIC_URL
from demetadataapp.models import *
from demetadataapp.forms import *


'''-----------------------
Home Page
-----------------------'''
# Home page
@login_required
@render_to("demetadataapp/home.html")
def home(request):
    existing_tables = TableUpload.objects.filter(has_metadata=True)
    return_tables = []
    # Return table structure:
    #   [
    #       {
    #           "table_name":"db_table_name",
    #           "related_tables":[(source_data_id,"db_table_name"),]
    #       }
    #   ]
    # collect geographys, extents, years of nometadata tables as front-end filters
    # collect related tables of nometadata table based on the following criteria:
    # 1. "geography_extent_subject" exactly match existing table
    #       a. collect all matched tables to put in related tables
    #       b. sort based on name 
    #          (in this case, year is the only difference, thus, 
    #           it's sorted based on year accedently in ascending order)
    # 2. if not 1, 
    #       a. find "subject" exactly match "subject" in existing table
    #           i. collect all matched tables to put in related tables
    #           ii. sort based on name (which will be geography in ascending order)
    #       b. find "subject" contained by "subject" in existing table
    #           i. collect all matched tables to append in ralated tables
    #           ii. sort based on name (which will be geography in ascending order)
    nometa_tables = TableUpload.objects.filter(has_metadata=False)
    request_year = request_geography = request_extent = request_search = None
    if request.method == 'GET':
        if 'year' in request.GET and request.GET['year']:
            request_year = request.GET['year']
        if 'geography' in request.GET and request.GET['geography']:
            request_geography = request.GET['geography'].lower()
        if 'extent' in request.GET and request.GET['extent']:
            request_extent = request.GET['extent'].lower()
        if 'search' in request.GET and request.GET['search']:
            request_search = request.GET['search'].lower()
    request_filters = (request_geography,request_extent,request_year)
        
    # collect existing geographys, extents, subjects, and years
    nometa_years = []
    nometa_geographys = []
    nometa_extents = []

    for table in nometa_tables:
        related_tables = []
        geography,extent,subject,txt_year = table.db_table.split("_")
        table_filters = (geography,extent,txt_year)
        flag = True
        for index,rf in enumerate(request_filters):
            if rf and (rf != table_filters[index]):
                flag = False
        if request_search and flag:
            if not request_search in table.db_table:
                flag = False

        # extract year
        if txt_year and txt_year.isdigit():
            year = int(txt_year)
            if not year in nometa_years:
                nometa_years.append(year)
        # extract geography
        if not geography.capitalize() in nometa_geographys:
            nometa_geographys.append(geography.capitalize())
        # extract extent
        if not extent.capitalize() in nometa_extents:
            nometa_extents.append(extent.capitalize())
        
        if flag:
            # build related table list
            find_table = "%s_%s_%s" % (geography,extent,subject)
            # Criteria 1
            for et in existing_tables:
                # if "geo_ext_sub" exactly matches existing table
                if find_table == "_".join(et.db_table.split("_")[:-1]):
                    related_tables.append((et.id,et.db_table))
            if related_tables:
                related_tables.sort(key = lambda x: x[1])
            else:
            # Criteria 2
                related_tables_2 = []
                for et in existing_tables:
                    exist_subject = et.db_table.split("_")[2]
                    # Criteria 2.a: if "sub" exactly matches existing table
                    if subject == exist_subject:
                        related_tables.append((et.id,et.db_table))
                    # Criteria 2.b: if "sub" and existing table contains one the other
                    # by checking if the shorter string is contained in the longer string
                    elif (subject if len(subject) < len(exist_subject) else exist_subject) in (subject if len(subject) > len(exist_subject) else exist_subject):
                        related_tables_2.append((et.id,et.db_table))
                if related_tables:
                    related_tables.sort(key = lambda x: x[1])
                if related_tables_2:
                    related_tables_2.sort(key = lambda x: x[1])
                    related_tables += related_tables_2
                    
            metadata_coverage = Coverage.objects.get_or_create(name=extent.capitalize())[0]
            metadata_geography = Geography.objects.get_or_create(name=geography.capitalize())[0]
            metadata_spatial_tables = SpatialTable.objects.filter(db_table_name=geography)
            if metadata_spatial_tables:
                metadata_geometry = metadata_spatial_tables[0]
            else:
                metadata_geometry = None
                    
            return_tables.append({
                "table_id": table.id,
                "table_name": table.db_table,
                "related_tables": related_tables,
                "metadata":{
                    "filepath": table.file_path,
                    "coverage": metadata_coverage.id,
                    "geography": metadata_geography.id,
                    "geometry": metadata_geometry.id if metadata_geometry else "",
                    "year": txt_year,
                    "title": subject,
                }
            })
            
    nometa_years.sort()
    nometa_geographys.sort()
    nometa_extents.sort()
    
    return {
        "nometa_tables": return_tables,
        "years": nometa_years,
        "geographys": nometa_geographys,
        "extents": nometa_extents,
    }

'''-----------------------
Metadata APIs
-----------------------'''
# Duplicate metadata of existing source data
@login_required
def duplicate_sourcedata(request):
    if request.method == 'GET':
        if ('copy_id' in request.GET and request.GET['copy_id']) and ('new_id' in request.GET and request.GET['new_id']):
            copy_table_id = int(request.GET['copy_id'])
            copy_table = SourceDataInventory.objects.get(id = copy_table_id)
            new_table_id = int(request.GET['new_id'])
            upload_table = TableUpload.objects.get(id = new_table_id)
            geography,extent,subject,txt_year = upload_table.db_table.split("_")
            new_table_title = copy_table.title.replace(str(copy_table.year),txt_year).replace(copy_table.geography.name.capitalize(),geography.capitalize()).replace(copy_table.geography.name.lower(),geography)
            new_table_macro_domain = copy_table.macro_domain.id
            new_table_subject_matter = copy_table.subject_matter.id
            new_table_year = txt_year
            new_geography = Geography.objects.get_or_create(name=geography.capitalize())[0]
            new_table_geography = new_geography.id
            new_coverage = Coverage.objects.get_or_create(name=extent.capitalize())[0]
            new_table_coverage = new_coverage.id
            new_table_source = copy_table.source.id
            new_table_source_website = copy_table.source_website
            new_table_location = upload_table.file_path
            new_table_metadata = new_table_id
            try:
                new_table_geometry = str(SpatialTable.objects.filter(db_table_name=geography)[0].id)
            except:
                new_table_geometry = ""
            new_table_description = copy_table.description.replace("by %s" % copy_table.geography.name.capitalize(),"by %s" % geography.capitalize()).replace("by %s" % copy_table.geography.name.lower(),"by %s" % geography)
            new_table_data_consideration = copy_table.data_consideration
            new_table_process_notes = copy_table.process_notes        
            
            redirect_url_parms = "id=%d" % new_table_id + \
                                 "&title=%s" % new_table_title + \
                                 "&macro_domain=%d" % new_table_macro_domain + \
                                 "&subject_matter=%d" % new_table_subject_matter + \
                                 "&year=%s" % new_table_year + \
                                 "&geography=%d" % new_table_geography + \
                                 "&coverage=%d" % new_table_coverage + \
                                 "&source=%d" % new_table_source + \
                                 "&source_website=%s" % new_table_source_website + \
                                 "&location=%s" % new_table_location + \
                                 "&metadata=%s" % new_table_metadata + \
                                 "&geometry=%s" % new_table_geometry + \
                                 "&description=%s" % new_table_description + \
                                 "&data_consideration=%s" % new_table_data_consideration + \
                                 "&process_notes=%s" % new_table_process_notes
            redirect_url = "%s/admin/demetadataapp/sourcedatainventory/add/?%s" % (ADMIN_ROOT_URL,redirect_url_parms)
            return HttpResponseRedirect(redirect_url)            
    else:
        return "Error: no related id found"

