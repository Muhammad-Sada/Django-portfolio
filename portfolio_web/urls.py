from django.urls import path
from .views import home_page, projects_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('projects/', projects_page, name='projects_page'),
]