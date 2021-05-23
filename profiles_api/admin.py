from django.contrib import admin

from profiles_api import models

# register userProfile with the admin site - makes accessible with admin interface
admin.site.register(models.UserProfile)

# Register your models here.
