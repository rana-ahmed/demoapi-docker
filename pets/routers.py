from rest_framework import routers

from .views import PetView

pet_router = routers.SimpleRouter()

pet_router.register(r'pets', PetView)
