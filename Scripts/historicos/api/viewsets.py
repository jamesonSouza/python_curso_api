from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from historicos.api.serializers import HistoricoDetalhesSerializer, HistoricosSerializer
from historicos.models  import Historicos


class HistoricosViewSet(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class =HistoricosSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset=Historicos.objects.filter(pk=pk)
        self.serializer_class=HistoricoDetalhesSerializer
        serializer= self.get_serializer(queryset,many=True)

        return Response(serializer.data)

