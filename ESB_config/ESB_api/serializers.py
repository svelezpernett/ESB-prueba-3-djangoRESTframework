from rest_framework import serializers
from ESB_api.models import *

class Cliente_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['cedula', 'nombre', 'apellido', 'telefono', 'correo']