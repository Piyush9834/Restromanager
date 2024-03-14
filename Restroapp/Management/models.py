from django.db import models
from django.contrib.auth.models import PermissionsMixin
from dj_rest_kit.models import BaseUUIDModel
from django.contrib.auth.base_user import AbstractBaseUser
from .constant import UserConstants
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, BaseUUIDModel):
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    mobile_no = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(unique=True)
    user_type = models.IntegerField(choices=UserConstants.get_user_type_choices(), null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager
    
    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = 'users'









class Customer(BaseUUIDModel):
    first_name = models.CharField(max_length=10, null=False, blank=False)
    Second_name = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=10, unique=True)
    purchesed_item = models.CharField(max_length=100)
    price = models.IntegerField()
    total_price = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = verbose_name_plural = _("Customers")
        
class Employee(BaseUUIDModel):
    first_name = models.CharField(max_length=10, null=False, blank=False)
    last_name = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    mobile = models.CharField(max_length=10, unique=True)
    joining_date = models.DateField(null=False, blank=True)
    salary = models.IntegerField()
    leave_count = models.CharField(max_length=10)
    address = models.CharField(max_length=40, null=False)
    image = models.ImageField()
    public_id = models.FileField()
    
    def __str__(self):
        return f"{self.first_name}"

class OldEmployee(BaseUUIDModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10, unique=True)
    date_of_joined = models.DateField()
    date_of_release = models.DateField()
    address = models.CharField(max_length=50)
    identity_card = models.FileField()
    
    def __str__(self):
        return f"{self.first_name}"
