from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from directory.serializers import RegionListSerializer, DistrictSerializer, CountrySerializer

from .models import User, Role, AppModule


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(source='role', read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'last_name', 'first_name', 'second_name', 'is_active', 'date_of_birthday', 'gender', 'phone_number', 'avatar', 'email',
            'date_joined', 'role', 'roles', 'password', 'country', 'region',
            'district', 'address', 'passport_series', 'passport_number', 'avatar')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator(), UniqueValidator(queryset=User.objects.all())],
            }
        }

    def create(self, validated_data, null=None):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.password = make_password(password)
        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data, ):
        instance.username = validated_data.get("username", instance.username)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.second_name = validated_data.get("second_name", instance.second_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.date_of_birthday = validated_data.get("date_of_birthday", instance.date_of_birthday)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.email = validated_data.get("email", instance.email)
        instance.date_joined = validated_data.get("date_joined", instance.date_joined)
        instance.role = validated_data.get("role", instance.role)
        instance.roles = validated_data.get("roles", instance.roles)
        instance.country = validated_data.get("country", instance.country)
        instance.region = validated_data.get("region", instance.region)
        instance.district = validated_data.get("district", instance.district)
        instance.address = validated_data.get("address", instance.address)
        instance.passport_series = validated_data.get("passport_series", instance.passport_series)
        instance.passport_number = validated_data.get("passport_number", instance.passport_number)
        password = validated_data.get("password", instance.password)
        if password:
            instance.password = make_password(password)
        else:
            instance.password = instance.password
        instance.save()
        return instance


class UserListPublicSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(source='role', read_only=True)
    country_detail = CountrySerializer(source='country', read_only=True)
    region_detail = RegionListSerializer(source='region', read_only=True)
    district_detail = DistrictSerializer(source='district', read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'last_name', 'first_name', 'second_name', 'is_active', 'date_of_birthday', 'gender', 'phone_number', 'avatar', 'email',
            'date_joined', 'role', 'roles', 'password', 'country', 'country_detail', 'region',
            'region_detail', 'district', 'district_detail', 'address', 'passport_series', 'passport_number',
            'avatar')


class UserListSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(source='role', read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'last_name', 'first_name', 'second_name', 'is_active', 'date_of_birthday', 'gender', 'phone_number', 'avatar', 'email',
            'date_joined', 'role', 'roles', 'password', 'country', 'region',
            'district', 'address', 'passport_series', 'passport_number', 'avatar')


class RelatedUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator(), UniqueValidator(queryset=User.objects.all())],
            }
        }


class RelatedUserPutSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'username': {
                'validators': [],
            }
        }


class ContentTypeSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField(method_name='get_permissions')

    class Meta:
        model = ContentType
        fields = ('id', 'model', 'permissions')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if hasattr(instance, 'extendedcontenttype'):
            ret['model'] = instance.extendedcontenttype.extend_name.upper()
        else:
            ret['model'] = ret['model'].upper()
        return ret

    def get_permissions(self, instance):
        permissions = Permission.objects.filter(content_type=instance.id)
        result = []
        for p in permissions:
            result.append(
                {"id": p.id, "name": p.codename.split('_')[0].upper()}
            )
        return result


class AppModuleSerializer(serializers.ModelSerializer):
    modules = ContentTypeSerializer(source='content_types', read_only=True, many=True)

    class Meta:
        model = AppModule
        fields = ('id', 'name', 'modules', 'sorting')


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.instance
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()
        return instance

