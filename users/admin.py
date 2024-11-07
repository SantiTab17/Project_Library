from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name',  'is_staff', 'phone_number')
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'address'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
