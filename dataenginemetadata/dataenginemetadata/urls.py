from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dataenginemetadata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # App URLs
    url(r'^demetadata/',include('demetadataapp.urls')),
    
    # 3rd party app url
    url(r'^chaining/', include('smart_selects.urls')),
]
