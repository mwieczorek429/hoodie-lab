from django.contrib import admin
from .models import Hoodie

@admin.register(Hoodie)
class HoodieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
