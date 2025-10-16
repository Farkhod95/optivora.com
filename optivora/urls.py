from django.urls import re_path, path

from optivora.views.banner import BannerView, BannerDetailView, BannerFieldInfoView, BannerViewList
from optivora.views.company_profile import CompanyProfileView, CompanyProfileDetailView, CompanyProfileFieldInfoView, \
    CompanyProfileViewList
from optivora.views.dashboard_stats import dashboard_stats
from optivora.views.downloadable_file import DownloadableFileView, DownloadableFileDetailView, \
    DownloadableFileFieldInfoView, DownloadableFileViewList
from optivora.views.equipment_category import EquipmentCategoryView, EquipmentCategoryDetailView, \
    EquipmentCategoryFieldInfoView, EquipmentCategoryViewList
from optivora.views.faq import FAQView, FAQDetailView, FAQFieldInfoView
from optivora.views.industry import IndustryView, IndustryDetailView, IndustryFieldInfoView, IndustryViewList
from optivora.views.inquiry import InquiryView, InquiryDetailView, InquiryFieldInfoView, InquiryViewList
from optivora.views.news_post import NewsPostView, NewsPostDetailView, NewsPostFieldInfoView
from optivora.views.partner import PartnerView, PartnerDetailView, PartnerFieldInfoView, PartnerViewList
from optivora.views.project import ProjectView, ProjectDetailView, ProjectFieldInfoView, ProjectViewList
from optivora.views.project_deliverable import ProjectDeliverableView, ProjectDeliverableDetailView, \
    ProjectDeliverableFieldInfoView
from optivora.views.project_image import ProjectImageView, ProjectImageDetailView, ProjectImageFieldInfoView, \
    ProjectImageViewList
from optivora.views.service import ServiceView, ServiceDetailView, ServiceFieldInfoView, ServiceViewList
from optivora.views.stat_item import StatItemView, StatItemDetailView, StatItemFieldInfoView
from optivora.views.testimonial import TestimonialView, TestimonialDetailView, TestimonialFieldInfoView

urlpatterns = [
    re_path(r'^company-profile$', CompanyProfileView.as_view(), name='company-profile-view'),
    path('company-profile/<int:pk>', CompanyProfileDetailView.as_view(), name='company-profile-detail-view'),
    path('company-profile/fields/', CompanyProfileFieldInfoView.as_view(), name='company-profile-fields-info'),
    path('company-profile/public', CompanyProfileViewList.as_view(), name='company-profile-public-info'),

    re_path(r'^industry$', IndustryView.as_view(), name='industry-view'),
    path('industry/<int:pk>', IndustryDetailView.as_view(), name='industry-detail-view'),
    path('industry/fields/', IndustryFieldInfoView.as_view(), name='industry-fields-info'),
    path('industry/public', IndustryViewList.as_view(), name='industry-public-info'),

# EquipmentCategory
    re_path(r'^equipment-category$', EquipmentCategoryView.as_view(), name='equipment-category-list'),
    path('equipment-category/<int:pk>', EquipmentCategoryDetailView.as_view(), name='equipment-category-detail'),
    path('equipment-category/fields/', EquipmentCategoryFieldInfoView.as_view(), name='equipment-category-fields'),
    path('equipment-category/public', EquipmentCategoryViewList.as_view(), name='equipment-category-public-info'),

    # Service
    re_path(r'^service$', ServiceView.as_view(), name='service-list'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service-detail'),
    path('service/fields/', ServiceFieldInfoView.as_view(), name='service-fields'),
    path('service/public', ServiceViewList.as_view(), name='service-public-info'),

    # Partner
    re_path(r'^partner$', PartnerView.as_view(), name='partner-list'),
    path('partner/<int:pk>', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/fields/', PartnerFieldInfoView.as_view(), name='partner-fields'),
    path('partner/public', PartnerViewList.as_view(), name='partner-public-info'),

    # Project
    re_path(r'^project$', ProjectView.as_view(), name='project-list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('project/fields/', ProjectFieldInfoView.as_view(), name='project-fields'),
    path('project/public', ProjectViewList.as_view(), name='project-public-info'),

    # ProjectDeliverable
    re_path(r'^project-deliverable$', ProjectDeliverableView.as_view(), name='project-deliverable-list'),
    path('project-deliverable/<int:pk>', ProjectDeliverableDetailView.as_view(), name='project-deliverable-detail'),
    path('project-deliverable/fields/', ProjectDeliverableFieldInfoView.as_view(), name='project-deliverable-fields'),

    # ProjectImage
    re_path(r'^project-image$', ProjectImageView.as_view(), name='project-image-list'),
    path('project-image/<int:pk>', ProjectImageDetailView.as_view(), name='project-image-detail'),
    path('project-image/fields/', ProjectImageFieldInfoView.as_view(), name='project-image-fields'),
    path('project-image/public', ProjectImageViewList.as_view(), name='project-image-public-info'),

    # StatItem
    re_path(r'^stat-item$', StatItemView.as_view(), name='stat-item-list'),
    path('stat-item/<int:pk>', StatItemDetailView.as_view(), name='stat-item-detail'),
    path('stat-item/fields/', StatItemFieldInfoView.as_view(), name='stat-item-fields'),

    # FAQ
    re_path(r'^faq$', FAQView.as_view(), name='faq-list'),
    path('faq/<int:pk>', FAQDetailView.as_view(), name='faq-detail'),
    path('faq/fields/', FAQFieldInfoView.as_view(), name='faq-fields'),

    # Inquiry
    re_path(r'^inquiry$', InquiryView.as_view(), name='inquiry-list'),
    path('inquiry/<int:pk>', InquiryDetailView.as_view(), name='inquiry-detail'),
    path('inquiry/fields/', InquiryFieldInfoView.as_view(), name='inquiry-fields'),
    path('inquiry/public', InquiryViewList.as_view(), name='inquiry-public-info'),

    # DownloadableFile
    re_path(r'^downloadable-file$', DownloadableFileView.as_view(), name='downloadable-file-list'),
    path('downloadable-file/<int:pk>', DownloadableFileDetailView.as_view(), name='downloadable-file-detail'),
    path('downloadable-file/fields/', DownloadableFileFieldInfoView.as_view(), name='downloadable-file-fields'),
    path('downloadable-file/public', DownloadableFileViewList.as_view(), name='downloadable-file-public-info'),

    # NewsPost
    re_path(r'^news-post$', NewsPostView.as_view(), name='news-post-list'),
    path('news-post/<int:pk>', NewsPostDetailView.as_view(), name='news-post-detail'),
    path('news-post/fields/', NewsPostFieldInfoView.as_view(), name='news-post-fields'),

    # Testimonial
    re_path(r'^testimonial$', TestimonialView.as_view(), name='testimonial-list'),
    path('testimonial/<int:pk>', TestimonialDetailView.as_view(), name='testimonial-detail'),
    path('testimonial/fields/', TestimonialFieldInfoView.as_view(), name='testimonial-fields'),

    re_path(r'^banner$', BannerView.as_view(), name='banner-list'),
    path('banner/<int:pk>', BannerDetailView.as_view(), name='banner-detail'),
    path('banner/fields/', BannerFieldInfoView.as_view(), name='banner-fields'),
    path('banner/public', BannerViewList.as_view(), name='banner-public-info'),

    path('dashboard/stats/', dashboard_stats, name='dashboard-stats'),
]
