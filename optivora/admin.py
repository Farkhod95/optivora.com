# apps/website/admin.py
from django.contrib import admin
from .models import (
    CompanyProfile,
    Industry,
    EquipmentCategory,
    Service,
    Partner,
    Project,
    ProjectDeliverable,
    ProjectImage,
    StatItem,
    FAQ,
    Inquiry,
    DownloadableFile,
    NewsPost,
    Testimonial, Banner, OurWork,
)


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    fields = (
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt', 'file', 'years_experience', 'equipment_categories', 'projects_supported',
        'international_partners', 'logo', 'email', 'phone', 'address', 'business_hours',
        'title', 'title_en', 'title_uz', 'title_ru', 'title_lt',
        'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
    )
    search_fields = ('name', 'email', 'phone', 'address')


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = (
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt',
        'slug', 'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
        'icon', 'order_index',
    )
    search_fields = ('name', 'slug', 'short_description', 'description')


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = (
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt',
        'slug',
        'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
        'order_index',
    )
    search_fields = ('name', 'slug', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = (
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt',
        'slug', 'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
        'icon', 'industries', 'equipment_categories', 'order_index',
    )
    search_fields = ('name', 'slug', 'short_description', 'description')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'website', 'order_index')
    fields = (
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt', 'country',
        'category', 'logo', 'website',
        'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
        'industries', 'equipment_categories', 'order_index',
    )
    search_fields = ('name', 'website', 'description')
    autocomplete_fields = ('country',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'country', 'region', 'district', 'is_featured', 'order_index')
    fields = (
        'title', 'title_en', 'title_uz', 'title_ru', 'title_lt',
        'slug', 'country', 'region', 'district', 'year',
        'scope', 'scope_en', 'scope_uz', 'scope_ru',
        'summary', 'summary_en', 'summary_uz', 'summary_ru',
        'featured_image', 'industries', 'equipment_categories', 'partners',
        'is_featured', 'order_index',
    )
    search_fields = ('title', 'slug', 'scope', 'summary')


@admin.register(ProjectDeliverable)
class ProjectDeliverableAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')
    fields = (
        'project',
        'name', 'name_en', 'name_uz', 'name_ru', 'name_lt',
    )
    search_fields = ('name', 'project__title')


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'order_index')
    fields = (
        'project', 'image',
        'caption', 'caption_en', 'caption_uz', 'caption_ru',
        'order_index',
    )
    search_fields = ('project__title', 'caption')


@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order_index')
    fields = (
        'label', 'label_en', 'label_uz', 'label_ru', 'label_lt',
        'value', 'order_index',
    )
    search_fields = ('label', 'value')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order_index')
    fields = (
        'question', 'question_en', 'question_uz', 'question_ru', 'question_lt',
        'answer', 'answer_en', 'answer_uz', 'answer_ru', 'answer_lt',
        'order_index',
    )
    search_fields = ('question', 'answer')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'email', 'inquiry_type', 'project_sector', 'status')
    fields = (
        'full_name',
        'company',
        'email', 'phone',
        'inquiry_type', 'project_sector', 'message', 'attachment',
        'consent_updates', 'status', 'ip_address', 'user_agent',
    )
    search_fields = ('full_name', 'company', 'email', 'phone', 'message')


@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_public')
    fields = (
        'title', 'title_en', 'title_uz', 'title_ru', 'title_lt',
        'category',
        'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
        'file', 'is_public',
    )
    search_fields = ('title', 'description')


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_at')
    fields = (
        'title', 'title_en', 'title_uz', 'title_ru', 'title_lt',
        'slug', 'category',
        'excerpt', 'excerpt_en', 'excerpt_uz', 'excerpt_ru', 'excerpt_lt',
        'body', 'body_en', 'body_uz', 'body_ru', 'body_lt',
        'cover_image', 'status', 'published_at',
    )
    search_fields = ('title', 'slug', 'excerpt', 'body')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'company', 'is_featured')
    fields = (
        'author_name', 'author_role', 'author_role_en', 'author_role_uz', 'author_role_ru', 'author_role_lt',
        'company',
        'quote', 'quote_en', 'quote_uz', 'quote_ru', 'quote_lt',
        'photo', 'is_featured',
    )
    search_fields = ('author_name', 'author_role', 'company', 'quote')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'is_featured')
    fields = (
        'order_index', 'title', 'title_en', 'title_uz', 'title_ru', 'title_lt', 'description', 'description_en', 'description_uz',
        'description_ru', 'description_lt', 'photo', 'is_featured',
    )
    search_fields = ('title', 'description')



@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'description', 'order_index')
    fields = (
        'order_index', 'title', 'title_en', 'title_uz', 'title_ru', 'title_lt', 'description', 'description_en', 'description_uz',
        'description_ru', 'description_lt', 'icon', 'type',
    )
    search_fields = ('title', 'description')