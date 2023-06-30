<template>
    <div class="row justify-content-center">
        <div class="col-5">
            <h3><strong>Busca Medicamentos PMVG</strong></h3>
        </div>
    </div>
    <div class="row justify-content-center searchrow">
        <div class="col-4">
            <select v-model="key" class="form-control">
                <option selected disabled value="">Filtro</option>
                <option v-for="data in selectdata" :key="data.field" :value="data.field">{{ data.str }}</option>
            </select>
        </div>
        <div class="col-4">
            <input v-model="query" placeholder="Entre com a chave de pesquisa" class="form-control">
        </div>
        <div class="col-4">
            <button type="button" class="btn btn-block btn-success text-center" @click="navigateTo(`/chave-${key}/${query}`)">Pesquisar</button>
        </div>    
    </div>
</template>

<script setup>

const query = ref('')
const key = ref('')

const selectdata = ref([
    {
        'field': 'principio_ativo',
        'str': 'Princípio Ativo'
    },
    {
        'field': 'cnpj',
        'str': 'CNPJ'
    },
    {
        'field': 'laboratorio',
        'str': 'Laboratório'
    },
    {
        'field': 'codigo_ggrem',
        'str': 'Código GGREM'
    },
    {
        'field': 'ean1',
        'str': 'EAN1'
    },
    {
        'field': 'ean2',
        'str': 'EAN2'
    },
    {
        'field': 'ean3',
        'str': 'EAN3'
    },
    {
        'field': 'produto',
        'str': 'Produto'
    },
    {
        'field': 'apresentacao',
        'str': 'Apresentação'
    },
    {
        'field': 'tipo_produto',
        'str': 'Tipo Produto'
    },
    {
        'field': 'classe_terapeutica',
        'str': 'Classe Terapêutica'
    },
    {
        'field': 'restricao_hospitalar',
        'str': 'Restrição Hospitalar'
    },
    {
        'field': 'regime_preco',
        'str': 'Regime preço'
    },
    {
        'field': 'cap', 
        'str': 'CAP'
    },
    {
        'field': 'confa87',
        'str': 'CONFAZ 87'
    },
    {
        'field': 'icsm0',
        'str': 'ICSM 0%'
    },
    {
        'field': 'lista_concessao_credito',
        'str': 'Lista Concessão Crédito'
    },
    {
        'field': 'comercializacao_2022',
        'str': 'Comercialização 2022'
    },
    {
        'field': 'tarja',
        'str': 'Tarja'
    },
])

</script>