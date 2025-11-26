from django.contrib import admin
from .models import Ministry, Objective

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    search_fields = ('name', 'acronym')

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'ministry')
    search_fields = ('title', 'ministry__name')
    list_filter = ('ministry',)
