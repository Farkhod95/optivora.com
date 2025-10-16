from modeltranslation.translator import register, TranslationOptions

from .models import CompanyProfile, Industry, EquipmentCategory, Service, Partner, Project, FAQ, ProjectImage


@register(CompanyProfile)
class CompanyProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'description')


@register(Industry)
class IndustryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


@register(EquipmentCategory)
class EquipmentCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(ProjectImage)
class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('caption',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'scope')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')