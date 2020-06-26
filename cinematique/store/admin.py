from django.contrib import admin

# Register your models here.
from .models import *;

admin.site.register(bollywood)
admin.site.register(hollywood)
admin.site.register(anime)
admin.site.register(web)