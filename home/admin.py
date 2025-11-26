from django.contrib import admin
from .models import DashboardStatistic

@admin.register(DashboardStatistic)
class DashboardStatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'icon')
    search_fields = ('title', 'description')
