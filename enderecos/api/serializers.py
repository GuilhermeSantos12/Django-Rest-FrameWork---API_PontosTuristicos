from rest_framework.serializers import ModelSerializer
from enderecos.models import Enderecos

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('id','linha1','linha2','cidade','estado','pais','latitude','longitude')