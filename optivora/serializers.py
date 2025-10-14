from rest_framework import serializers

from .models import CompanyProfile


# Tarjima asosiy serializeri
class LocaleSerializer(serializers.ModelSerializer):
    name_en = serializers.CharField(allow_blank=False)
    name_uz = serializers.CharField(allow_blank=False)
    name_ru = serializers.CharField(allow_blank=False)



class CompanyProfileSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('id', 'name', 'logo', 'email', 'phone', 'address', 'business_hours')
        extra_kwargs = {
            'code': {"required": True},
            'name_en': {"required": True},
            'name_uz': {"required": True},
            'name_ru': {"required": True},
        }


class CompanyProfileListSerializer(LocaleSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('id', 'name', 'logo', 'email', 'phone', 'address', 'business_hours')