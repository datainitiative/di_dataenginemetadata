from demetadataapp.models import *
from demetadataapp.forms import *
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

# Import from general utilities
from util import *

# Import from app
from dataenginemetadata.settings import ROOT_APP_URL, ADMIN_ROOT_URL

# Import function from views.py
#from demetadataapp.views import down_as_zip

# Customized Admin Form for Look-up Table Model
## Macro Domain Admin
class MacroDomainAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(MacroDomain, MacroDomainAdmin)

## Subject Matter Admin
class SubjectMatterAdmin(admin.ModelAdmin):
    fields = ['name','macro_domain']
    list_display = ('id','name','macro_domain')
    list_filter = ['macro_domain']
    list_per_page = 15
admin.site.register(SubjectMatter, SubjectMatterAdmin)

## Geography Admin
class GeographyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(Geography, GeographyAdmin)

## Coverage Admin
class CoverageAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(Coverage, CoverageAdmin)

## Format Admin
class FormatAdmin(admin.ModelAdmin):
    fields = ['name','extension']
    list_display = ('id','name','extension')
    list_per_page = 15
admin.site.register(Format, FormatAdmin)

## Source Admin
class SourceAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(Source, SourceAdmin)

## Contributor Admin
class ContributorAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(Contributor, ContributorAdmin)

## Spatial Table Admin
class SpatialTableAdmin(admin.ModelAdmin):
    fields = ['id','name','db_table_name','db_table_id']
    list_display = ('id','name','db_table_name','db_table_id')
    list_per_page = 15
admin.site.register(SpatialTable, SpatialTableAdmin)

## Tag Admin
class TagAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
    list_per_page = 15
admin.site.register(Tag,TagAdmin)

## Table Upload Admin
class TableUploadAdmin(admin.ModelAdmin):
    fields = ['id','db_table','file_path','has_metadata']
    list_display = ('id','db_table','file_path','has_metadata')
    search_fields = ['db_table','file_path']
    list_per_page = 15
admin.site.register(TableUpload, TableUploadAdmin)

## Data Tables Admin
class DataTableAdmin(admin.ModelAdmin):
    fields = ['id','table_name','db_table']
    list_display = ('id','table_name','db_table')
    search_fields = ['table_name','db_table']
    list_per_page = 15
admin.site.register(DataTable, DataTableAdmin)

# Table Metadata Admin
class TableMetadataAdmin(admin.ModelAdmin):
    fields = ['metadata']
    list_display = ['id','metadata']
    list_per_page = 10
admin.site.register(TableMetadata,TableMetadataAdmin)

#class SourcedataMacrodomainListFilter(SimpleListFilter):
#    title = "Domain"
#    parameter_name = 'macro_domain__id__exact'
#    def lookups(self,request,model_admin):
#        macrodomains = MacroDomain.objects.all()
#        return([(macrodomain.id,macrodomain.name) for macrodomain in macrodomains])
#
#    def queryset(self,request,queryset):
#        if self.value():
#            return queryset.filter(macro_domain__id__exact=self.value())
#        else:
#            return queryset
#
#class SourcedataSubjectmatterListFilter(SimpleListFilter):
#    title = "Subdomain"
#    parameter_name = 'subject_matter__id__exact'
#    def lookups(self,request,model_admin):
#        subjectmatters = SubjectMatter.objects.all()
#        if request.GET.get("macro_domain__id__exact"):
#            subjectmatters = SubjectMatter.objects.filter(macrodomain__id__exact=request.GET.get("macro_domain__id__exact"))
#        return([(subjectmatter.id,subjectmatter.name) for subjectmatter in subjectmatters])
#
#    def queryset(self,request,queryset):
#        if self.value():
#            if request.GET.get("macro_domain__id__exact"):
#                subjectmatters = SubjectMatter.objects.filter(macrodomain__id__exact=request.GET.get("macro_domain__id__exact"))
#                # if SubjectMatter doesn't match MacroDomain when MacroDomain gets changed
#                if not subjectmatters.filter(id=self.value()):
#                    return queryset
#                return queryset.filter(subject_matter__id__exact=self.value())
#        else:
#            return queryset

# Customized Admin Form for Source Data Inventory Model
class SourceDataInventoryAdmin(admin.ModelAdmin):
    actions = ['download']
    fields = ['id','title','macro_domain','subject_matter','coverage','geography',
        'year','source','source_website','location','metadata','geometry',
        'description','data_consideration','process_notes']    
    list_display = ('title','macro_domain','get_subject_matter_name',
        'coverage','geography','year','source','_get_metadata_link')
    list_filter = ['macro_domain','subject_matter','coverage','geography','source','year']    
    search_fields = ['title']
    list_per_page = 10
    
    form = SourceDataInventoryAdminForm
    
#    # By defualt use the Change page form
#    form = SourceDataInventoryAdminChangeForm
#    def get_form(self,request,obj=None,**kwargs):
#        if not obj: # obj is None, this is ADD page, then use the Add page form
#            self.form = SourceDataInventoryAdminAddForm
#        return super(SourceDataInventoryAdmin,self).get_form(request,obj,**kwargs)

    # Redirect to page "Dataset to add" page after adding new source data
    def response_add(self, request, obj, post_url_continue="../%s/"):
        if '_save' in request.POST:
            return HttpResponseRedirect("%s/home/" % ROOT_APP_URL)
        elif '_continue' in request.POST:
            return HttpResponseRedirect("%s/admin/demetadataapp/dataset/add/?id=%d&tables=%d&name=%s" % (ADMIN_ROOT_URL,obj.id,obj.id,obj.title))
        else:
            return super(MyModelAdmin, self).response_add(request, obj, post_url_continue)  

    # Display Subject Matter name
    def get_subject_matter_name(self,obj):
        return obj.subject_matter.name
    get_subject_matter_name.short_description = "Subdomain"    
    
    # Download as CSV
    def download(self,request,queryset):
        sourcedata_ids = []
        for s in queryset:
            sourcedata_ids.append(s.id)
        return down_as_zip(request,sourcedata_ids)
    download.short_description = "Download selected source data tables"
admin.site.register(SourceDataInventory, SourceDataInventoryAdmin)

# Admin for Dataset Model
class DatasetAdmin(admin.ModelAdmin):
    fields = ['id','nid','name','contributor','tables','tags','large_dataset','update_date']
    list_display = ('id','nid','name','contributor','_get_str_tables','_get_str_tags','_is_large_dataset','_get_metadata_link','update_date')
    list_filter = ['tags','tables','tables__macro_domain','tables__subject_matter','tables__source','tables__coverage','tables__geography','tables__year','contributor']
    list_per_page = 10
    filter_horizontal = ['tables','tags']
    readonly_fields = ['update_date']
admin.site.register(Dataset,DatasetAdmin)