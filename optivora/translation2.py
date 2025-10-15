from modeltranslation.translator import register, TranslationOptions

from .models import CompanyProfile, Industry, EquipmentCategory, Service, Partner, Project, FAQ


@register(CompanyProfile)
class CompanyProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'description')


@register(Industry)
class IndustryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


@register(EquipmentCategory)
class EquipmentCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Industry)
class IndustryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'scope')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')