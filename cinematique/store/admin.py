from django.contrib import admin

# Register your models here.
from .models import *;

admin.site.register(Bollywood)
admin.site.register(Hollywood)
admin.site.register(Anime)
admin.site.register(Web)