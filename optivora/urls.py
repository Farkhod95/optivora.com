from django.urls import re_path, path

from optivora.views.company_profile import CompanyProfileView, CompanyProfileDetailView, CompanyProfileFieldInfoView
from optivora.views.industry import IndustryView, IndustryDetailView, IndustryFieldInfoView

urlpatterns = [
    re_path(r'^company-profile/$', CompanyProfileView.as_view(), name='company-profile-view'),
    path('company-profile/<int:pk>', CompanyProfileDetailView.as_view(), name='company-profile-detail-view'),
    path('company-profile/fields/', CompanyProfileFieldInfoView.as_view(), name='company-profile-fields-info'),

    re_path(r'^industry/$', IndustryView.as_view(), name='industry-view'),
    path('industry/<int:pk>', IndustryDetailView.as_view(), name='industry-detail-view'),
    path('industry/fields/', IndustryFieldInfoView.as_view(), name='industry-fields-info'),
]
