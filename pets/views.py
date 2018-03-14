from rest_framework.viewsets import ModelViewSet

from .models import Pet
from .serializers import PetSerializer


class PetView(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
