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
    Testimonial,
)


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    fields = ('name', 'name_en', 'name_uz', 'name_ru', 'logo', 'email', 'phone', 'address', 'business_hours', 'title', 'title_en', 'title_uz', 'title_ru', 'description', 'description_en', 'description_uz', 'description_ru',)
    search_fields = ('name', 'email', 'phone', 'address')


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = ('name', 'name_en', 'name_uz', 'name_ru', 'slug', 'short_description', 'description', 'icon', 'order_index', )
    search_fields = ('name', 'slug', 'short_description', 'description')


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = ('name', 'name_en', 'name_uz', 'name_ru', 'slug', 'description', 'order_index', )
    search_fields = ('name', 'slug', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order_index')
    fields = ('name', 'name_en', 'name_uz', 'name_ru', 'slug', 'short_description', 'description', 'icon', 'industries', 'equipment_categories', 'order_index', )
    search_fields = ('name', 'slug', 'short_description', 'description')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'website', 'order_index')
    fields = ('name', 'name_en', 'name_uz', 'name_ru', 'category', 'logo', 'website', 'description', 'industries', 'equipment_categories', 'order_index', )
    search_fields = ('name', 'website', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'country', 'region', 'district', 'is_featured', 'order_index')
    fields = (
        'title', 'title_en', 'title_uz', 'title_ru', 'slug', 'country', 'region', 'district', 'year', 'scope', 'summary',
        'featured_image', 'industries', 'equipment_categories', 'partners',
        'is_featured', 'order_index',
    )
    search_fields = ('title', 'slug', 'scope', 'summary')


@admin.register(ProjectDeliverable)
class ProjectDeliverableAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')
    fields = ('project', 'name', 'name_en', 'name_uz', 'name_ru', )
    search_fields = ('name', 'project__title')


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'order_index')
    fields = ('project', 'image', 'caption', 'order_index', )
    search_fields = ('project__title', 'caption')


@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order_index')
    fields = ('label', 'value', 'order_index', )
    search_fields = ('label', 'value')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order_index')
    fields = ('question', 'answer', 'order_index', )
    search_fields = ('question', 'answer')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'email', 'inquiry_type', 'project_sector', 'status')
    fields = (
        'full_name', 'company', 'email', 'phone',
        'inquiry_type', 'project_sector', 'message', 'attachment',
        'consent_updates', 'status', 'ip_address', 'user_agent', 
    )
    search_fields = ('full_name', 'company', 'email', 'phone', 'message')


@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_public')
    fields = ('title', 'category', 'description', 'file', 'is_public', )
    search_fields = ('title', 'description')


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_at')
    fields = ('title', 'slug', 'category', 'excerpt', 'body', 'cover_image', 'status', 'published_at', )
    search_fields = ('title', 'slug', 'excerpt', 'body')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'company', 'is_featured')
    fields = ('author_name', 'author_role', 'company', 'quote', 'photo', 'is_featured', )
    search_fields = ('author_name', 'author_role', 'company', 'quote')
