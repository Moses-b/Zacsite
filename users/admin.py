from django.contrib import admin

from .models import profile, Location

class ProfileAdmin(admin.ModelAdmin):
   pass

class LocationAdmin(admin.ModelAdmin):
   pass

admin.site.register(profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)