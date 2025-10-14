from django_filters.rest_framework import FilterSet

from optivora.models import CompanyProfile, Industry


class CompanyProfilesFilter(FilterSet):

    class Meta:
        model = CompanyProfile
        fields = {
            'name': ['exact'],
            'email': ['exact'],
        }


class IndustrysFilter(FilterSet):

    class Meta:
        model = Industry
        fields = {
            'name': ['exact'],
            'slug': ['exact'],
        }