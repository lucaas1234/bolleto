from django.db import models

class Cliente (models.Model):

	usuario = models.ForeignKey('auth.User')
	cnpj = models.CharField(max_length= 14)


	def __str__(self):
		return self.usuario.first_name + " " + self.usuario.last_name
	


class Cedente(models.Model):

	cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE)
	razao_social = models.CharField(max_length=100)
	cnpj = models.CharField(max_length=14)
	banco = models.CharField(max_length=3)
	agencia = models.CharField(max_length=5)
	agencia_dv = models.CharField(max_length=1)
	conta = models.CharField(max_length=12)
	conta_dv = models.CharField(max_length=1)
	convenio = models.CharField(max_length=6)

	def __str__(self):
		return self.razao_social

class Sacado (models.Model):

		cnpj = models.CharField(max_length=14)
		nome = models.CharField(max_length=50)
		endereco = models.CharField(max_length=100)
		bairro = models.CharField(max_length=50)
		cidade = models.CharField(max_length=50)
		uf = models.CharField(max_length=2)
	
		def __str__(self):
			return self.nome

class Contrato(models.Model):

		sacado = models.ForeignKey(Sacado,on_delete = models.CASCADE)
		cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE)
		data = models.DateField()
		valor = models.DecimalField(max_digits = 11, decimal_places = 2)
		multa = models.DecimalField(max_digits = 5, decimal_places = 2)
		juros = models.DecimalField(max_digits = 5, decimal_places = 2)

		def __str__(self):
			return "No.:" + str(self.id) + " - " + self.cliente.__str__()

class Prestacao(models.Model):

		contrato = models.ForeignKey(Contrato,on_delete = models.CASCADE) 
		data_vencimento = models.DateField() 
		valor = models.DecimalField(max_digits = 11, decimal_places = 2)
		data_pagamento = models.DateField()
		valor_multa = models.DecimalField(max_digits = 5, decimal_places = 2)
		valor_juros = models.DecimalField(max_digits = 5, decimal_places = 2)






