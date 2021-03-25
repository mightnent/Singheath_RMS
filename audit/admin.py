from django.contrib import admin

# Register your models here.
from .models import Tenant

class TenantAdmin(admin.ModelAdmin):
    list_display = ('id','business_name','institution',)
    list_display_links = ('id','business_name',)
    search_fields = ('business_name',)
    list_per_page = 25
admin.site.register(Tenant,TenantAdmin)