
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("More Info", {
            "fields": ("profile_picture",),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("MoreInfo", {
            "fields": ("profile_picture",),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
