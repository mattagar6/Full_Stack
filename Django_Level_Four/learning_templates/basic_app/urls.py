from django.conf.urls import url
from basic_app import views

# need to define app_name to utilize the relative urls with template tagging
# django looks for the global variable 'app_name'
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'^other/$', views.other, name = 'other'),
    
]
