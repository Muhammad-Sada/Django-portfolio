from django.shortcuts import render
from .models import Project


def home_page(request):
    projects = Project.objects.all().order_by('-id')[:3]
    return render(request, 'home_page.html',{'projects': projects})

def projects_page(request):
    projects = Project.objects.all().order_by('-id')
    return render(request, 'project_page.html', {'projects': projects})

