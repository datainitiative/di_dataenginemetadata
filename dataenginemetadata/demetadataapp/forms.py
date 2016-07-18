from django.contrib import admin
from django import forms
from django.forms.widgets import *
from django.db import models
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Snippet import to use the admin FilterSelectMultiple widget in normal forms
from django.contrib.admin.widgets import FilteredSelectMultiple

# Import from general utilities
from util import *

from demetadataapp.models import *

class SourceDataInventoryAdminForm(forms.ModelForm):
    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'size':'50'}),required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'size':'50'}),required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
    data_consideration = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
    process_notes = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),required=False)

## Custome SourceDataInventory Admin Model Form for CHANGE Page
#class SourceDataInventoryAdminChangeForm(forms.ModelForm):
##    upload_file = forms.FileField(required=False)
#    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'size':'50'}),required=False)
#    title = forms.CharField(widget=forms.TextInput(attrs={'size':'50'}),required=False)
#    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
#    data_consideration = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
#    process_notes = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),required=False)
##    macro_domain = forms.ModelChoiceField(queryset=MacroDomain.objects.all(),widget=forms.Select(attrs={'onchange':'get_subjectmatter();'}))
#
#    def save(self, commit=True):
#        model = super(SourceDataInventoryAdminChangeForm, self).save(commit=False)
#        
##        # Transform local path to server path
##        if self.cleaned_data['location'].find(SOURCE_DATA_ROOT_PATH_ORIGIN) >= 0:
##            model.location = self.cleaned_data['location'].replace(SOURCE_DATA_ROOT_PATH_ORIGIN,SOURCE_DATA_ROOT_PATH_LOCAL)        
#        
#        if self.cleaned_data['location'] != None:
#            upload_file = self.cleaned_data['location']
#            upload_file_extension = upload_file[upload_file.index('.')+1:]
#            
#            # Get the format for the file extension from lookup table "Format"
#            try:
#                # Full-text search on column Format
#                ## Need PostgreSQL Setup:
#                ## 1. Add a column to hold a tsvector
#                ##    ALTER TABLE inventory_format ADD COLUMN ext_tsv tsvector;
#                ## 2. Add a trigger to update the ext_tsv column whenever a record is inserted or updated
#                ##    CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE ON inventory_format FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(ext_tsv, 'pg_catalog.english', extension);
#                ## 3. Create an index on ext_tsv to make searches more efficient
#                ##    CREATE INDEX inventory_format_ext_tsv ON inventory_format USING gin(ext_tsv);
#                ## 4. If there is already rechords in the inventory_format table, update the ext_tsv for those records
#                ##    UPDATE inventory_format SET ext_tsv=to_tsvector(extension);
#                ## 5. SQL example
#                ##    SLECT extension FROM inventory_format WHERE ext_tsv @@ plainto_tsquery('serch words');
#                q = upload_file_extension
#                model.format = Format.objects.extra(
#                    where=['ext_tsv @@ plainto_tsquery(%s)'],params=[q])[0]
#            except:# Create new format if it dosenot exist
#                add_format = Format(name=upload_file_extension,extension=upload_file_extension)
#                add_format.save()
#                model.format = Format.objects.get(extension=upload_file_extension)
#        
#        if commit:
#            model.save()
#            
#        return model
#    
#    class Meta:
#        model = SourceDataInventory
#        fields = ['upload_file','file_name','format','title','macro_domain','subject_matter',
#        'coverage','geography','year','source','source_website','location','geometry',
#        'description','data_consideration','process_notes']
#        
## Custome SourceDataInventory Admin Model Form for ADD page
#class SourceDataInventoryAdminAddForm(forms.ModelForm):
#    upload_file = forms.FileField(required=False)
#    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'size':'50'}),required=True)
#    title = forms.CharField(widget=forms.TextInput(attrs={'size':'50'}),required=False)
#    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
#    data_consideration = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':6}),required=False)
#    process_notes = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),required=False)
##    macro_domain = forms.ModelChoiceField(queryset=MacroDomain.objects.all(),widget=forms.Select(attrs={'onchange':'get_subjectmatter();'})) 
#
#    def save(self, commit=True):
#        model = super(SourceDataInventoryAdminAddForm, self).save(commit=False)
#        
#        if self.cleaned_data['upload_file'] != None:
#            upload_file = self.cleaned_data['upload_file'].name
#            upload_file_name = upload_file[:upload_file.index('.')]
#            upload_file_extension = upload_file[upload_file.index('.')+1:]
#            model.file_name = upload_file_name
#            model.file_size = self.cleaned_data['upload_file'].size
#            if self.cleaned_data['location'].find(SOURCE_DATA_ROOT_PATH_ORIGIN) >= 0:
#                model.location = self.cleaned_data['location'].replace(SOURCE_DATA_ROOT_PATH_ORIGIN,SOURCE_DATA_ROOT_PATH_LOCAL)
#                
#            # Get the format for the file extension from lookup table "Format"
#            try:
#                # Full-text search on column Format
#                q = upload_file_extension
#                model.format = Format.objects.extra(
#                    where=['ext_tsv @@ plainto_tsquery(%s)'],params=[q])[0]
#            except:# Create new format if it dosenot exist
#                add_format = Format(name=upload_file_extension,extension=upload_file_extension)
#                add_format.save()
#                model.format = Format.objects.get(extension=upload_file_extension)
#        
#        if commit:
#            model.save()
#            
#        return model
#    
#    class Meta:
#        model = SourceDataInventory
#        fields = ['upload_file','file_name','format','title','macro_domain','subject_matter',
#                'coverage','geography','year','source','source_website','location','geometry',
#                'description','data_consideration','process_notes']