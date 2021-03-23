from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProjectModel, Language

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    projects = ProjectModel.objects.all()
    all_languages = Language.objects.all()
    for project in projects:
        languages = project.languages.all().values_list("name", flat=True)
        project.style = " ".join(languages)
    context = {
        "projects": projects,
        "languages": all_languages,

    }
    return HttpResponse( template.render(context, request))
