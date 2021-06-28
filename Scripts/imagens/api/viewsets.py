from imagens.api.serializers import ImagensHistoricoSerializer
from imagens.models import ImagensHistorico
from rest_framework import viewsets

class ImagensHistoricoViewSet(viewsets.ModelViewSet):
    queryset =ImagensHistorico.objects.all()
    serializer_class =ImagensHistoricoSerializer


