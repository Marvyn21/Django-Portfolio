from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProjectModel

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    projects = ProjectModel.objects.all()
    context = {
        "projects": projects

    }
    return HttpResponse( template.render(context, request))
