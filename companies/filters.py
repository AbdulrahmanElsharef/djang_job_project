import django_filters
from board.models import Employer


class EmployerFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employer
        fields=['name','industry','Profile']
