from django.contrib import admin

from .models import Company, TechStack

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website', 'created']
    list_filter = ['created']


@admin.register(TechStack)
class TechStack(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created']
    list_filter = ['created']