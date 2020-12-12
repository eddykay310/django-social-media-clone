from django.urls import path
from . import views

app_name ='groups'

urlpatterns = [
    path('', views.ListGroups.as_view(),name='all_groups'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/<slug>',views.GroupDetail.as_view(),name='group_detail')
]