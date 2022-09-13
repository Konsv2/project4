from django.urls import path, re_path
from . import views
#from mysite.search import views
from .views import SearchResultsList
        
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("search/", SearchResultsList.as_view(), name="search_results"),

    
]
