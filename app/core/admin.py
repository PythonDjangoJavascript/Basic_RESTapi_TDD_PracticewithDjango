from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Custom Admin Page"""

    ordering = ["id"]
    list_display = ["email", "name"]

    """This is for admin fields in admin page"""
    fieldsets = (
        (None, {
            "fields": (
                "email", "password"
            )
        }),
        (_("Personal Info"), {
            "fields": (
                "name",
            )
        }),
        (_("Permissions"), {
            "fields": (
                "is_active", "is_staff", "is_superuser"
            )
        }),
        (_("Important dates"), {
            "fields": (
                "last_login",
            ),
        })
    )

    """Add a new object(User)"""
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",
            ),
            "fields": (
                "email", "name", "password1", "password2"
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.ProfileFeedItem)
