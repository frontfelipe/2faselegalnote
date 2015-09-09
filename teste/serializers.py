from django.forms import widgets
from rest_framework import serializers
from teste.models import Processos


class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processos
        fields = ('id', 'user', 'num_processo', 'dados_processo', 'data_pub')