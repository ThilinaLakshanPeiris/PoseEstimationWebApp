from rest_flex_fields import FlexFieldsModelViewSet, FlexFieldsModelSerializer
from rest_framework import serializers
# from test_api.models import Emp, Region, Depot, STCMachineDistribution, STCMachinesDistribution, User,FuelUser,\
#     UserLevel,InsuranceCompany,VehicleCategory,VehicleDetail,IncomingFuel,FuelType,RegionDistribution,\
#      MainStock,ClosingTable ,Requisition ,PumpMethod,Designation,Institute,Transaction,OtherDistribution,STCVehicleDistribution,Contractor,\
#     ContractorDistribution, DefaultFuelPrice
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from WebApp.models import user

# class userSuperSerializer(serializers.ModelSerializer):
#     class Meta:
#         mode = User
#         fields = ('__all__')
class userSerializer(serializers.ModelSerializer):
    class Meta:
        mode = user
        fields = ('__all__')

# class RegionSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = Region
#         fields = ('__all__')
        

# class DepotSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = Depot
#         fields = ('__all__')
#         expandable_fields = {'reg': (RegionSerializer, {'source': 'region_id', 'fields': ['region_id', 'region_txt']})}

# class UserLevelSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = UserLevel
#         fields = ('__all__')

# class UserSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = FuelUser
#         fields = ('__all__')
#         depth = 1
#         #fields = (FuelUser.fuel_user_id, FuelUser.User.username)                          
#         expandable_fields = {'region': (RegionSerializer, {'source': 'region_id', 'fields': ['region_id', 'region_txt']}),
#                              'depot': (DepotSerializer, {'source': 'depot_id', 'fields': ['depot_id', 'depot_txt']}),
#                              'userlevel': (UserLevelSerializer, {'source': 'level_id', 'fields': ['level_id', 'level_name']}),
#                             }
       
""" 
Extend user and autohnticatons

"""

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
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
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

# class UpdateRequisitionSerializer(serializers.ModelSerializer):
#     pump_qty = serializers.FloatField(required=True)
    
#     class Meta:
#         model = Requisition
#         fields = ('pump_qty', 'status')
#         extra_kwargs = {
#             'pump_qty': {'required': True},
#             'status': {'required': True},
#         }            

# class DefaultFuelPriceSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model  = DefaultFuelPrice
#         fields = ('__all__')  
#         expandable_fields = {'fuel_type': (FuelTypeSerializer, {'source': 'pump_type_id', 'fields': ['pump_type_id', 'pump_text']})}
