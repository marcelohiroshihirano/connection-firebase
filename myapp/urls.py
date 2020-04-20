from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^list/$',views.list_courses, name='list'),  
    url(r'^list/(?P<id>[-\w]+)/$',views.course_details, name='list'),  
    #url(r'^list/(\d+)/$/$', views.course_details),
    #url(r'^about/$', views.about, name="about"),

]