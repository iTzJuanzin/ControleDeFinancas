from django.db import models

class transacao(models.Model):


    class Tipo(models.TextChoices):
        ENTRADA = 'entrada', 'Entrada'
        SAIDA = 'saida', 'Saida'

    tipo = models.CharField(max_length=10, choices=Tipo.choices)

    descricao = models.CharField(max_length=100)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        sinal = "+"  if self.tipo == "entrada" else "-"
        return f"{sinal} R$ {self.valor} - {self.descricao}"