from django.db import models
from pacientes.models import Pacientes

class Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)

    data_hora   =models.DateTimeField(blank=False,null=False)

    data_criacao = models.DateTimeField(auto_now_add=True)

    cancelado   =models.BooleanField(default=False)

    obj =models.TextField(blank=True,null=True)

    tipo    =models.CharField(max_length=100,blank=True,null=True)

    #chave estrangeira de paciente e n pode ser blanco ou nulo, agendamento sem paciente n existe
    id_paciente =models.ForeignKey(Pacientes,on_delete=models.CASCADE,related_name='agendamentos',blank=False,null=False)
    


    class Meta:
        managed=True
        db_table="agendamentos"
        # esse parametro é para nao haver pacientes na mesma data e hora e com o mesmo paciente
        unique_together=('data_hora','id_paciente')
