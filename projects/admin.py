from django.contrib import admin
from .models import Project, Indicator

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'ministry', 'status', 'budget')
    search_fields = ('title', 'ministry__name', 'description')
    list_filter = ('status', 'ministry')

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'unit')
    search_fields = ('name', 'project__title')
    list_filter = ('project', 'unit')
