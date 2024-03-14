from django.db import models
from .models import *
from dj_rest_kit.serializers import DynamicFieldsUUIDModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
class UserSerializer(DynamicFieldsUUIDModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "email",
            "mobile_no",
            
            "user_type",
           
            "is_active",
            "password",
            "password_confirmation",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("email already exists!")
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password_confirmation = validated_data.pop('password_confirmation', None)
        
        if password != password_confirmation:
            raise ValueError({"password do not match!"})
        custom_user = super().create(validated_data)
        if password is not None:
            custom_user.set_password(password)
        custom_user.save()
        return custom_user
    
    def update(self, instance, validated_data):
        
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        
        super().update(instance, validated_data) 
        return instance   
            
                 
    

class CustomerSerializer(DynamicFieldsUUIDModelSerializer):
    model = Customer
    fields = ['uuid', 'first_name', 'second_name', 'mobile', ' purchesed_item', 'total_price']
    
    
    
    
class EmployeeSerializer(DynamicFieldsUUIDModelSerializer):
    model = Employee
    fields = ['uuid', 'first_name', 'last_name', 'email', 'mobile', 'joining_date', 'salary', 'leave_count', 'address', 'image', 'public_id' ] 
    
   
class OldEmployeeSerializer(DynamicFieldsUUIDModelSerializer):
    model = OldEmployee 
    fields = ['uuid', 'first_name', 'last_name', 'date_of_joined', 'date_of_release', 'address', 'identity_card']     