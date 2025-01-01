from django.shortcuts import render
from .models import Project, PersonalInfo

def home(request):
    personal_info = PersonalInfo.objects.first()  
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'Base/home.html', {
        'personal_info': personal_info,
        'projects': projects
    })