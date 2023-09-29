from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'mobile', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email', 'mobile')
    ordering = ('-date_joined', )


admin.site.register(User, UserAdmin)
