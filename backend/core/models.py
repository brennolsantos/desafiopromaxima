from django.db import models

# Create your models here.
class MedPMGV(models.Model):

	PN_CHOICES = [
		('P', 'Positiva'),
		('N', 'Negativa')
	]

	principio_ativo = models.CharField(max_length=3000, blank=True, null=True)
	cnpj = models.CharField(max_length=18, blank=True, null=True)
	laboratorio = models.CharField(max_length=100, blank=True, null=True)
	codigo_ggrem = models.CharField(max_length=15, blank=True, null=True)
	registro = models.CharField(max_length=13, blank=True, null=True)
	ean1 = models.CharField(max_length=13, blank=True, null=True)
	ean2 = models.CharField(max_length=13, blank=True, null=True)
	ean3 = models.CharField(max_length=13, blank=True, null=True)
	produto = models.CharField(max_length=100, blank=True, null=True)
	apresentacao = models.CharField(max_length=3000, blank=True, null=True)
	classe_terapeutica = models.CharField(max_length=100, blank=True, null=True)
	tipo_produto = models.CharField(max_length=100, blank=True, null=True)
	regime_preco = models.CharField(max_length=50, blank=True, null=True)
	pf_sem = models.FloatField(blank=True, null=True)
	pf0 = models.FloatField(blank=True, null=True)
	pf12 = models.FloatField(blank=True, null=True)
	pf17 = models.FloatField(blank=True, null=True)
	pf17_alc = models.FloatField(blank=True, null=True)
	pf17_5 = models.FloatField(blank=True, null=True)
	pf17_5_alc = models.FloatField(blank=True, null=True)
	pf18 = models.FloatField(blank=True, null=True)
	pf18_alc = models.FloatField(blank=True, null=True)
	pf19 = models.FloatField(blank=True, null=True)
	pf20 = models.FloatField(blank=True, null=True)
	pf21 = models.FloatField(blank=True, null=True)
	pf22 = models.FloatField(blank=True, null=True)
	pmvg_sem_imposto = models.FloatField(blank=True, null=True)
	pmvg0 = models.FloatField(blank=True, null=True)
	pmvg12 = models.FloatField(blank=True, null=True)
	pmvg17 = models.FloatField(blank=True, null=True)
	pmvg17_alc = models.FloatField(blank=True, null=True)
	pmvg17_5 = models.FloatField(blank=True, null=True)
	pmvg17_5_alc = models.FloatField(blank=True, null=True)
	pmvg18 = models.FloatField(blank=True, null=True)
	pmvg18_alc = models.FloatField(blank=True, null=True)
	pmvg19 = models.FloatField(blank=True, null=True)
	pmvg20 = models.FloatField(blank=True, null=True)
	pmvg21 = models.FloatField(blank=True, null=True)
	pmvg22 = models.FloatField(blank=True, null=True)
	restricao_hospitalar = models.BooleanField(blank=True, null=True)
	CAP = models.BooleanField(blank=True, null=True)
	confaz87 = models.BooleanField(blank=True, null=True)
	icms0 = models.BooleanField(blank=True, null=True)
	analise_recursal = models.CharField(max_length=100,blank=True, null=True)
	lista_concessao_credito = models.CharField(max_length=1, choices=PN_CHOICES, blank=True, null=True)
	comercializacao_2022 = models.BooleanField(blank=True, null=True)
	tarja = models.CharField(max_length=50, blank=True, null=True)
