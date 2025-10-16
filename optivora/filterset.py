from django_filters.rest_framework import FilterSet
from django_filters import rest_framework as filters

from optivora.models import CompanyProfile, Industry, EquipmentCategory, Service, Partner, Project, ProjectDeliverable, \
    ProjectImage, StatItem, FAQ, Inquiry, DownloadableFile, NewsPost, Testimonial, Banner


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


class EquipmentCategoryFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = EquipmentCategory
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'order_index': ['exact'],
        }


class ServiceFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = Service
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'industries': ['exact'],
            'equipment_categories': ['exact'],
            'order_index': ['exact'],
        }


class PartnerFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = Partner
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'industries': ['exact'],
            'equipment_categories': ['exact'],
            'order_index': ['exact'],
        }


class ProjectFilter(FilterSet):
    year__gte = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year__lte = filters.NumberFilter(field_name='year', lookup_expr='lte')
    is_featured = filters.BooleanFilter(field_name='is_featured')

    class Meta:
        model = Project
        fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'country': ['exact'],
            'region': ['exact'],
            'district': ['exact'],
            'industries': ['exact'],
            'equipment_categories': ['exact'],
            'partners': ['exact'],
            'is_featured': ['exact'],
            'order_index': ['exact'],
        }


class ProjectDeliverableFilter(FilterSet):
    class Meta:
        model = ProjectDeliverable
        fields = {
            'id': ['exact'],
            'project': ['exact'],
            'name': ['exact', 'icontains'],
        }


class ProjectImageFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = ProjectImage
        fields = {
            'id': ['exact'],
            'project': ['exact'],
            'caption': ['exact', 'icontains'],
            'order_index': ['exact'],
        }


class StatItemFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = StatItem
        fields = {
            'id': ['exact'],
            'label': ['exact', 'icontains'],
            'value': ['exact', 'icontains'],
            'order_index': ['exact'],
        }


class FAQFilter(FilterSet):
    order_index__gte = filters.NumberFilter(field_name='order_index', lookup_expr='gte')
    order_index__lte = filters.NumberFilter(field_name='order_index', lookup_expr='lte')

    class Meta:
        model = FAQ
        fields = {
            'id': ['exact'],
            'question': ['exact', 'icontains'],
            'order_index': ['exact'],
        }


class InquiryFilter(FilterSet):
    created_from = filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_to = filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Inquiry
        fields = {
            'id': ['exact'],
            'full_name': ['exact', 'icontains'],
            'company': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'phone': ['exact', 'icontains'],
            'inquiry_type': ['exact'],
            'project_sector': ['exact'],
            'status': ['exact'],
        }


class DownloadableFileFilter(FilterSet):
    class Meta:
        model = DownloadableFile
        fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'category': ['exact'],
            'is_public': ['exact'],
        }


class NewsPostFilter(FilterSet):
    published_from = filters.IsoDateTimeFilter(field_name='published_at', lookup_expr='gte')
    published_to = filters.IsoDateTimeFilter(field_name='published_at', lookup_expr='lte')

    class Meta:
        model = NewsPost
        fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'category': ['exact'],
            'status': ['exact'],
        }


class TestimonialFilter(FilterSet):
    class Meta:
        model = Testimonial
        fields = {
            'id': ['exact'],
            'author_name': ['exact', 'icontains'],
            'author_role': ['exact', 'icontains'],
            'company': ['exact', 'icontains'],
            'is_featured': ['exact'],
        }


class BannersFilter(FilterSet):
    class Meta:
        model = Banner
        fields = {
            'title': ['exact'],
        }