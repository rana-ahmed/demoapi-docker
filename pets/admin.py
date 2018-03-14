from django.contrib import admin
from .models import Pet

admin.sites.register(Pet)
