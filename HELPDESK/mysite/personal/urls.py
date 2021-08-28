from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('home/', views.home_screen_view, name='home'),
    path('duties/', views.assign_duties, name='duties'),
    path('issues/', views.raise_issues, name='issues'),
    path('staff/', views.staff_members, name='staff'),
]


