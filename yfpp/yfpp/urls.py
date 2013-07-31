from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^favicon\.ico$', redirect_to, {'url': '/static/favicon.ico'}, name='favicon'),
    # url(r'^$', direct_to_template, {'template': 'yfpp/address_form.html'}, name='home'),
    # url(r'^$', direct_to_template, {'template': 'yfpp/address_form.html'}, name='home'), 
    url(r'^$', TemplateView.as_view(template_name="yfpp/address_form.html")),       
#    url(r'^$', direct_to_template, {'template': 'yfpp/thanks.html'}, name='thanks'),
    # url(r'^privacy/', direct_to_template, {'template': 'yfpp/privacy.html'}, name='thanks'),
    url(r'^privacy/', TemplateView.as_view(template_name="yfpp/privacy.html")),      
    url(r'^fucking-check/', 'yfpp.views.fucking_check', name='fucking_check'),
    url(r'^results/', 'yfpp.views.results', name='results'),
    url(r'^client/', 'yfpp.views.client', name='client'),
    # url(r'^yfpp/', include('yfpp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()









# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# # from django.contrib import admin
# # admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'yfpp.views.home', name='home'),
#     # url(r'^yfpp/', include('yfpp.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )
