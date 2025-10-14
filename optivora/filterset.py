from django_filters.rest_framework import FilterSet

from optivora.models import CompanyProfile


class CompanyProfilesFilter(FilterSet):

    class Meta:
        model = CompanyProfile
        fields = {
            'name': ['exact'],
            'email': ['exact'],
        }
