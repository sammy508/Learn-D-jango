# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

@admin.register(UserModel)
class CleanUserAdmin(UserAdmin):
    # ONLY fields that actually exist in your model
    list_display = ['email', 'role', 'is_staff', 'is_active', 'created_at']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    
    # Simplified fieldsets - no unwanted fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Role & Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    # Minimal add form - only email + password + role
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role'),
        }),
    )