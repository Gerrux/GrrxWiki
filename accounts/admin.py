from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserUpdateForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('User Information', {'fields': ('email',)}),
        ('Personal Information', {'fields': ('profile_picture',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    filter_horizontal = ()
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
