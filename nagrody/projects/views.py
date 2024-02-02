from django.shortcuts import render
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# Create your views here.
from projects.models import Project
from .forms import NagrodyForms


def project_index(request):
    projects=Project.objects.all()
    context={
        "projects": projects
    }
    return render(request,"projects/project_index.html",context)


def nagroda_forma(request):
    context={}
    
    form=NagrodyForms(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        form.save()
    
    context['form']=form
    return render(request,"nagrody/nagrody_forma.html",context)
    