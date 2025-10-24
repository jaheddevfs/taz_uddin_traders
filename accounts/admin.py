# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'phone')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address')}),
    )