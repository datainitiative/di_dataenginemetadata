from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('demetadataapp.views',
	# Home page URL
	url(r'^home/$','home'),
	
	# Metadata APIs
	url(r'^api/duplicate_sourcedata/$','duplicate_sourcedata'),
)