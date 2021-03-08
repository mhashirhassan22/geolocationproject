from django.contrib import admin
from .models import Location, Favorites

# Register your models here.

class LocAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude','longitude','user')

class FavAdmin(admin.ModelAdmin):
    list_display = ('server', 'photo_id', 'secret', 'user')

admin.site.register(Location, LocAdmin)
admin.site.register(Favorites, FavAdmin)