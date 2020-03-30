from django.contrib import admin
from .models import *


# class Admin (admin.ModelAdmin):
#     list_display = [field.name for field in User._meta.fields]
#     # list_display = ['login', 'surname', 'name', 'email']
#
#     # inlines = []
#     exclude = ['password']
#
#     list_filter = ['name']
#     search_fields = ['email', 'mobile']
#
#     class Meta:
#         model = User
#
#
# admin.site.register(User, Admin)
