from rest_framework import serializers
from .models import Dados

class DadosSerializer(serializers.ModelSerializer):
    reset_contador = serializers.BooleanField(write_only=True)  # Campo de escrita apenas para o botão de reset

    class Meta:
        model = Dados
        fields = '__all__'
