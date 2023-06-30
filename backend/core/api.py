from rest_framework import viewsets
from rest_framework.response import Response
from core.models import MedPMGV
from core.serializers import MedPMGVSerializer

class MedPMGVAPI(viewsets.ModelViewSet):

	queryset = MedPMGV.objects.all()
	serializer_class = MedPMGVSerializer

	def list(self, request):
		principio_ativo = request.query_params.get('principio_ativo')
		cnpj = request.query_params.get('cnpj')
		laboratorio = request.query_params.get('laboratorio')
		codigo_ggrem = request.query_params.get('codigo_ggrem')
		ean1 = request.query_params.get('ean1')
		ean2 = request.query_params.get('ean2')
		ean3 = request.query_params.get('ean3')
		produto = request.query_params.get('produto')
		tipo_produto = request.query_params.get('tipo_produto')
		apresentacao = request.query_params.get('apresentacao')
		classe_terapeutica = request.query_params.get('classe_terapeutica')
		regime_preco = request.query_params.get('regime_preco')
		restricao_hospitalar = request.query_params.get('restricao_hospitalar')
		cap = request.query_params.get('cap')
		confaz87 = request.query_params.get('confaz_87')
		icms0 = request.query_params.get('icms0')
		lista_concessao_credito = request.query_params.get('lista_concessao_credito')
		comercializacao_2022 = request.query_params.get('comercializao_2022')
		tarja = request.query_params.get('tarja')

		bool_values = {
			'Sim': True, 
			'Não': False,
			'sim': True,
			'não': False,
			'SIM': True,
			'NÃO': False 
		}

		pn_values = {
			'positiva': 'P',
			'POSITIVA': 'P',
			'Positiva': 'P',
			'negativa': 'N',
			'Negativa': 'N',
			'NEGATIVA': 'N'
		}

		try:
			if(type(restricao_hospitalar) == str) restricao_hospitalar = restricao_hospitalar.strip()
			if(type(cap) == str) cap = cap.strip()
			if(type(confaz87) == str) confaz87 = cap.strip()
			if(type(icms0) == str) icms0 = icms0.strip()
			if(type(lista_concessao_credito) == str) lista_concessao_credito = lista_concessao_credito.strip()
			if(type(comercializacao_2022) == str) comercializacao_2022= comercializacao_2022.strip()

			restricao_hospitalar = bool_values[restricao_hospitalar]
			cap = bool_values[cap]
			confaz87 = bool_values[confaz87]
			icms0 = bool_values[icms0]
			lista_concessao_credito = pn_values[lista_concessao_credito]
			comercializacao_2022 = bool_values[comercializacao_2022]

			queryset = self.queryset
			queryset = queryset.filter(principio_ativo__icontains=principio_ativo) if principio_ativo is not None else queryset 
			queryset = queryset.filter(cnpj__icontains=cnpj) if cnpj is not None else queryset 
			queryset = queryset.filter(laboratorio__icontains=laboratorio) if laboratorio is not None else queryset 
			queryset = queryset.filter(codigo_ggrem__icontains=codigo_ggrem) if codigo_ggrem is not None else queryset
			queryset = queryset.filter(ean1__icontains=ean1) if ean1 is not None else queryset 
			queryset = queryset.filter(ean2__icontains=ean2) if ean2 is not None else queryset 
			queryset = queryset.filter(ean3__icontains=ean3) if ean3 is not None else queryset 
			queryset = queryset.filter(produto__icontains=produto) if produto is not None else queryset 
			queryset = queryset.filter(tipo_produto__icontains=tipo_produto) if tipo_produto is not None else queryset 
			queryset = queryset.filter(apresentacao__icontains=apresentacao) if apresentacao is not None else queryset
			queryset = queryset.filter(classe_terapeutica__icontains=classe_terapeutica) if classe_terapeutica is not None else queryset 
			queryset = queryset.filter(regime_preco__icontains=regime_preco) if regime_preco is not None else queryset
			queryset = queryset.filter(restricao_hospitalar=restricao_hospitalar) if restricao_hospitalar is not None else queryset 
			queryset = queryset.filter(CAP=cap) if cap is not None else queryset 
			queryset = queryset.filter(confaz87=confaz87) if confaz87 is not None else queryset 
			queryset = queryset.filter(icms0=icms0) if icms0 is not None else queryset
			queryset = queryset.filter(lista_concessao_credito=lista_concessao_credito) if lista_concessao_credito is not None else queryset
			queryset = queryset.filter(comercializacao_2022=comercializacao_2022) if comercializacao_2022 is not None else queryset
			queryset = queryset.filter(tarja__icontains=tarja) if tarja is not None else queryset 

			serializer = self.serializer_class(queryset, many=True)

			return Response(serializer.data, status=200)
		except Exception as e:
			return Response([], status=204)
