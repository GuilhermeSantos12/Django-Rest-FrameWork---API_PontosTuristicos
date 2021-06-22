from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
