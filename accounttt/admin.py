from django.contrib import admin
from .models import Profileee


@admin.register(Profileee)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone', 'address', 'tg_id']

    #list_display = [field.user for field in Profileee._meta.fields]