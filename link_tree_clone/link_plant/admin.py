from django.contrib import admin
from link_plant.models import Links, Profile
# Register your models here.


admin.site.register([Profile, Links])