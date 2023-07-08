import django_filters
from board.models import Job


class JobFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields=['name','des','job_type','category','employer',]
