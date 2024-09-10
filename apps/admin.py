from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models import User


#
# from apps.models import User, News, PhoneNumber, AdvImage, Adv
#
#
# # Register your models here.
# class PhoneNumberStackedInline(StackedInline):
#     model = PhoneNumber
#     min_num = 1
#     extra = 0
#
#
# class AdvImageStackedInline(StackedInline):
#     model = AdvImage
#
#
# @admin.register(User)
# class UserModelAdmin(UserAdmin):
#     list_display = 'username', 'email', 'first_name', 'last_name'
#     list_display_links = 'username', 'email'
#     inlines = [PhoneNumberStackedInline]
#
#
# @admin.register(News)
# class NewsModelAdmin(ModelAdmin):
#     list_display = 'id', 'views_count', 'created_at'
#
#
# @admin.register(Adv)
# class AdvModelAdmin(ModelAdmin):
#     list_display = 'id',
#     inlines = [AdvImageStackedInline]


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = 'phone_number', 'type'
    fieldsets = (
        (None, {"fields": ("phone_number", "type")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("usable_password", "password1", "password2"),
            },
        ),
    )
    ordering = ("phone_number",)
