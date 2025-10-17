from rest_framework import serializers

from directory.serializers import RegionListPublicSerializer, DistrictListPublicSerializer, CountryListSerializer
from .models import (CompanyProfile, Industry, EquipmentCategory, Service, Partner, Project,
                     ProjectDeliverable, ProjectImage, StatItem, FAQ,
                     Inquiry, DownloadableFile, NewsPost, Testimonial, Industry, Banner, OurWork
                     )


# Tarjima asosiy serializeri
class LocaleSerializer(serializers.ModelSerializer):
    name_en = serializers.CharField(allow_blank=False)
    name_uz = serializers.CharField(allow_blank=False)
    name_ru = serializers.CharField(allow_blank=False)

    title_en = serializers.CharField(allow_blank=False)
    title_uz = serializers.CharField(allow_blank=False)
    title_ru = serializers.CharField(allow_blank=False)

    label_en = serializers.CharField(allow_blank=False)
    label_uz = serializers.CharField(allow_blank=False)
    label_ru = serializers.CharField(allow_blank=False)

    description_en = serializers.CharField(allow_blank=False)
    description_uz = serializers.CharField(allow_blank=False)
    description_ru = serializers.CharField(allow_blank=False)


class BaseLocaleSerializer(serializers.ModelSerializer):
    """
    Dinamik ko‘p tilli serializer:
    Modelda mavjud bo‘lgan *_en/_uz/_ru maydonlar avtomatik qo‘shiladi.
    """
    TRANSLATABLE_BASES = [
        # eng ko‘p uchraydiganlar
        'name', 'title', 'label', 'description',
        'summary', 'caption', 'excerpt', 'body', 'scope',
        'question', 'answer', 'quote', 'author_role', 'company',
    ]
    LANGS = ['en', 'uz', 'ru']
    REQUIRED_BASES = {'name', 'title', 'label', 'question', 'answer'}  # muhim maydonlar

    def get_fields(self):
        fields = super().get_fields()
        model = getattr(self.Meta, 'model', None)
        if not model:
            return fields

        # Modeldagi real maydonlar to‘plami
        model_field_names = {f.name for f in model._meta.get_fields()}

        for base in self.TRANSLATABLE_BASES:
            for lang in self.LANGS:
                f_name = f"{base}_{lang}"
                if f_name in model_field_names:
                    fields[f_name] = serializers.CharField(
                        allow_blank=False,
                        required=(base in self.REQUIRED_BASES)
                    )
        return fields


class CompanyProfileSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = (
        'id', 'name', 'name_en', 'name_uz', 'name_ru', 'logo', 'email', 'phone', 'address', 'business_hours', 'title',
        'title_en', 'title_uz', 'title_ru', 'description', 'description_en', 'description_uz', 'description_ru', 'file',
        'years_experience', 'equipment_categories', 'projects_supported', 'international_partners',)
        extra_kwargs = {
            'name_en': {"required": True},
            'name_uz': {"required": True},
            'name_ru': {"required": True},
        }


class CompanyProfileListSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = (
        'id', 'name', 'name_en', 'name_uz', 'name_ru', 'logo', 'email', 'phone', 'address', 'business_hours', 'title',
        'title_en', 'title_uz', 'titleru', 'description', 'description_en', 'description_uz', 'description_ru', 'file',
        'years_experience', 'equipment_categories', 'projects_supported', 'international_partners',)


class IndustrySerializer(LocaleSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'slug', 'description', 'icon',
                  'order_index')
        extra_kwargs = {
            'name_en': {"required": True},
            'name_uz': {"required": True},
            'name_ru': {"required": True},
        }


class IndustryListPublicSerializer(LocaleSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'slug', 'description', 'icon',
                  'order_index')


class EquipmentCategorySerializer(BaseLocaleSerializer):
    class Meta:
        model = EquipmentCategory
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class EquipmentCategoryPublicListSerializer(BaseLocaleSerializer):
    class Meta:
        model = EquipmentCategory
        fields = ('name', 'slug')

class ServiceSerializer(BaseLocaleSerializer):
    industries = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), many=True, required=False
    )
    equipment_categories = serializers.PrimaryKeyRelatedField(
        queryset=EquipmentCategory.objects.all(), many=True, required=False
    )

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class PartnerSerializer(BaseLocaleSerializer):
    industries = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), many=True, required=False
    )
    equipment_categories = serializers.PrimaryKeyRelatedField(
        queryset=EquipmentCategory.objects.all(), many=True, required=False
    )

    class Meta:
        model = Partner
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')

class PartnerListPublicSerializer(BaseLocaleSerializer):

    class Meta:
        model = Partner
        fields =( 'name', 'category', 'website')


class ProjectSerializer(BaseLocaleSerializer):
    industries = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), many=True, required=False
    )
    equipment_categories = serializers.PrimaryKeyRelatedField(
        queryset=EquipmentCategory.objects.all(), many=True, required=False
    )
    partners = serializers.PrimaryKeyRelatedField(
        queryset=Partner.objects.all(), many=True, required=False
    )
    country_detail = CountryListSerializer(source="country", read_only=True)
    region_detail = RegionListPublicSerializer(source="region", read_only=True)
    district_detail = DistrictListPublicSerializer(source="district", read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class ProjectListSerializer(BaseLocaleSerializer):
    industries = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), many=True, required=False
    )
    equipment_categories = serializers.PrimaryKeyRelatedField(
        queryset=EquipmentCategory.objects.all(), many=True, required=False
    )
    partners = serializers.PrimaryKeyRelatedField(
        queryset=Partner.objects.all(), many=True, required=False
    )

    industries_detail = IndustryListPublicSerializer(source="industries", many=True, read_only=True)
    equipment_categories_detail = EquipmentCategoryPublicListSerializer(source="equipment_categories", many=True,
                                                                  read_only=True)
    partners_detail = PartnerListPublicSerializer(source="partners", many=True, read_only=True)

    country_detail = CountryListSerializer(source="country", read_only=True)
    region_detail = RegionListPublicSerializer(source="region", read_only=True)
    district_detail = DistrictListPublicSerializer(source="district", read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class ProjectDeliverableSerializer(BaseLocaleSerializer):
    class Meta:
        model = ProjectDeliverable
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class ProjectImageSerializer(BaseLocaleSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class StatItemSerializer(BaseLocaleSerializer):
    class Meta:
        model = StatItem
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class FAQSerializer(BaseLocaleSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class InquirySerializer(BaseLocaleSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'
        read_only_fields = ('id', 'updated_time', 'created_by', 'updated_by')


class DownloadableFileSerializer(BaseLocaleSerializer):
    class Meta:
        model = DownloadableFile
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class NewsPostSerializer(BaseLocaleSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class TestimonialSerializer(BaseLocaleSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class BannerSerializer(BaseLocaleSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')


class OurWorkSerializer(BaseLocaleSerializer):
    class Meta:
        model = OurWork
        fields = '__all__'
        read_only_fields = ('id', 'created_time', 'updated_time', 'created_by', 'updated_by')