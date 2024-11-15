from django.contrib import admin
from trips.models import Trip, Note
# Register your models here.

admin.site.register([Trip, Note])
