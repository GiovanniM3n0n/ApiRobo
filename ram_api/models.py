from django.db import models

class Dados(models.Model):
    sensor = models.BooleanField(default=False)
    botao = models.BooleanField(default=False)
    liga_robo = models.BooleanField(default=False)
    reset_contador = models.BooleanField(default=False)
    valor_contagem = models.IntegerField(default=0)

    def __str__(self):
        return f"Sensor: {self.sensor}, Botao: {self.botao}, LigaRobo: {self.liga_robo}, ResetContador: {self.reset_contador}, Valor Contagem: {self.valor_contagem}"

    def resetar_contador(self):
        self.valor_contagem = 0
        self.save()
