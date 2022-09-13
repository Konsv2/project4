from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.decorators.cache import cache_page

#from django.contrib.auth.models import Project
#from .filters import ProjectFilter

def project_index(request):
    projects = Project.objects.order_by('?')
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
     
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
    
          
    

class SearchResultsList(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "project_index.html"

    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Project.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )