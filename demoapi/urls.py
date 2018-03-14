from django.contrib import admin
from django.urls import path

from pets.routers import pet_router

urlpatterns = [
    path('admin/', admin.site.urls),
] + pet_router.urls
