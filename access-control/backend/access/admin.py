from django.contrib import admin
from .models import AccessPoint, AccessEvent

@admin.register(AccessPoint)
class AccessPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'is_active')
    search_fields = ('name', 'location')
    list_filter = ('is_active',)

@admin.register(AccessEvent)
class AccessEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'person_name', 'access_point', 'authorized', 'timestamp')
    search_fields = ('person_name', 'user__username', 'access_point__name')
    list_filter = ('authorized', 'access_point')
