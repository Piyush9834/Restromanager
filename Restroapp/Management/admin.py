from dj_rest_kit.admin import BaseAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from . import models

admin.site.register(models.Customer)

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile_no', 'email', 'user_type', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email', 'mobile_no')
    list_filter = ('user_type', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile_no', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )




@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name", "email", "mobile", "joining_date", "salary", "leave_count", "address", "image", "public_id"]
    search_fields = ["first_name", "last_name", "email", "mobile", "address"]
    list_filter = ["joining_date"]
    date_hierarchy = "joining_date"
    
@admin.register(models.OldEmployee)
class OldEmployee(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name", "mobile_no", "date_of_joined", "date_of_release", "address",
                    "identity_card"
                    
                    ]
    search_fields = ["first_name"]