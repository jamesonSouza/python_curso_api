from imagens.api.serializers import ImagensHistoricoSerializer
from rest_framework import serializers
from historicos.models import Historicos

class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model =Historicos
        fields  ='__all__'    

class HistoricoDetalhesSerializer(serializers.ModelSerializer):
    imagens = ImagensHistoricoSerializer(many=True,read_only=True)

    class Meta:
        model =Historicos
        fields=[
             'id_historico',
    'data'    ,
    'aparecimentos_sintomas' ,
    'duracao_sintomas'   ,
    'local_dor'  ,
    'tipo_dor'    ,
    'conclusao'   ,
    'id_agendamento' ,

            'imagens'
        ]