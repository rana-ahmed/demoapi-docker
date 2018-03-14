from rest_framework.viewsets import ModelViewSet

from .models import Pet


class PetView(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Pet.objects.all()
