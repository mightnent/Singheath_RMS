from django.contrib import admin

# Register your models here.
from .models import TenantLocation

class TenantLocationAdmin(admin.ModelAdmin):
    list_display = ('id','name','institution',)
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 25
admin.site.register(TenantLocation,TenantLocationAdmin)