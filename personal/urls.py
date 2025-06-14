from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('thoughts/', views.thought_list, name='thought_list'),
    path('thoughts/<slug:slug>/', views.thought_detail, name='thought_detail'),
    path('about/', views.about, name='about')
]

