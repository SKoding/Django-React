from django.contrib import admin
from django.contrib.gis import admin as gisAdmin
from .models import farm, farmer, partner

# Register your models here.
class farmAdmin(gisAdmin.GeoModelAdmin):
    list_display = ('id','grower_id','area',)
    search_fields = ('grower_id',)
    ordering = ('id',)

class farmerAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','is_active','is_staff','income',)

class partnerAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact','web')

gisAdmin.site.register(farm, farmAdmin)
admin.site.register(farmer, farmerAdmin)
admin.site.register(partner, partnerAdmin)
