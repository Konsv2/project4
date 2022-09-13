from django.contrib.auth.models import Project
import django_filters
from django.db.models import Q

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='atte',
        lookup_expr='contains'
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'image' ]
        
class ProjectFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_filter', label='Cerca')

    class Meta:
        model = Project
        fields = ['q']

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(sku__iexact=value))