from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosDeltalhesSerializer, AgendamentosSerializer

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class=AgendamentosSerializer

    @action(detail=True,methods=['get'])
    def detalhes(self,resquest, pk=None, *args, **kwargs):
        queryset = Agendamentos.objects.filter(pk=pk)
        self.serializer_class=AgendamentosDeltalhesSerializer
        serializer = self.get_serializer(queryset,many=True)

        return Response(serializer.data)

