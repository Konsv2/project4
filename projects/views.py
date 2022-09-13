from django.shortcuts import render
from projects.models import Project
import random

items = list(Product.objects.all())

# change 3 to how many random items you want
random_items = random.sample(items, 6)
# if you want only a single random item
random_item = random.choice(items)


def project_index(request):
    
    items = list(Project.objects.all())

    # change 3 to how many random items you want
    random_items = random.sample(items, 6)
    # if you want only a single random item
    projects = random.choice(items)
    
   # projects = Project.objects.order_by('?')[0]

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
