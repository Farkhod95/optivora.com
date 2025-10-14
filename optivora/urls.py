from django.urls import re_path, path

from optivora.views.company_profile import CompanyProfileView, CompanyProfileDetailView, CompanyProfileFieldInfoView

urlpatterns = [
    re_path(r'^company-profile/$', CompanyProfileView.as_view(), name='company-profile-view'),
    path('company-profile/<int:pk>', CompanyProfileDetailView.as_view(), name='company-profile-detail-view'),
    path('company-profile/fields/', CompanyProfileFieldInfoView.as_view(), name='company-profile-fields-info'),
]
