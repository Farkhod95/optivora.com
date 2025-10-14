from rest_framework import serializers

from .models import CompanyProfile, Industry


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



class CompanyProfileSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'logo', 'email', 'phone', 'address', 'business_hours')
        extra_kwargs = {
            'name': {"required": True},
            'name_en': {"required": True},
            'name_uz': {"required": True},
            'name_ru': {"required": True},
        }


class CompanyProfileListSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'logo', 'email', 'phone', 'address', 'business_hours')


class IndustrySerializer(LocaleSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'slug', 'short_description', 'description', 'icon', 'order_index')
        extra_kwargs = {
            'name': {"required": True},
            'name_en': {"required": True},
            'name_uz': {"required": True},
            'name_ru': {"required": True},
        }


class IndustryListSerializer(LocaleSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name', 'name_en', 'name_uz', 'name_ru', 'slug', 'short_description', 'description', 'icon', 'order_index')