from rest_framework.viewsets import ModelViewSet
from enderecos.models import Enderecos
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer 