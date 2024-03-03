from django.contrib import admin
from .models import Hoodie, Size, HoodieSize

@admin.register(Hoodie)
class HoodieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(HoodieSize)
class HoodieSizeAdmin(admin.ModelAdmin):
    pass