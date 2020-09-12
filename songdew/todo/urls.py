from django.conf.urls import url

from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^new/$',views.CreateList.as_view(),name='create'),
    url(r'^by/(?P<username>[-\w]+)/$',views.TodoList.as_view(),name='for_user'),
    ]
