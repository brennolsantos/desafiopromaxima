<script setup>
import { writeFile } from 'xlsx';
import { utils } from 'xlsx'

const route = useRoute()

const query = ref(route.params.query)
const key = ref(route.params.key)

const data  = await $fetch(`http://localhost:8080/medpmgv/?${route.params.key}=${route.params.query}`)

const show = ref(true) 

const detail = ref("Nenhuma coluna selecionada")

var lines_to_import = []

const filename = ref('')

const filexport = () =>
{
    let data_list = [ ];
    let rows = [];
    let name = filename

    if(name.length == 0)
    {
        window.alert('Nome do Arquivo em Branco!');
        return false;
    }

    if(lines_to_import.length == 0)
    {
        window.alert('Nenhum registro selecionado!');
        return false;
    }

    data_list = data;

    data_list = data_list.filter(d => lines_to_import.includes(d.id));
    data_list.map((data) => {
        rows.push({
            'PRINCIPIO_ATIVO': data.principio_ativo,
            'CNPJ': data.cnpj,
            'LABORATORIO': data.laboratorio,
            'CODIGO GGREM': data.codigo_ggrem,
            'REGISTRO': data.registro,
            'EAN 1': data.ean1,
            'EAN 2': data.ean2,
            'EAN 3': data.ean3,
            'PRODUTO': data.produto,
            'APRESENTAÇÃO': data.apresentacao,
            'CLASSE TERAPEUTICA': data.classe_terapeutica,
            'TIPO PRODUTO': data.tipo_produto,
            'REGIME PREÇO': data.regime_preco,
            'PF SEM IMPOSTO': data.pf_sem,
            'PF 0%': data.pf0 == null ? '' : data.pf0,
            'PF 12%': data.pf12 == null ? '' : data.pf12,
            'PF 17%': data.pf17 == null ? '' : data.pf17,
            'PF 17% ALC': data.pf17_alc == null ? '' : data.pf17_alc,
            'PF 17.5%': data.pf17_5 == null ? '' : data.pf17_5,
            'PF 17.5% ALC': data.pf17_5_alc == null ? '' : data.pf17_5_alc,
            'PF 18%': data.pf18 == null ? '' : data.pf18,
            'PF 18% ALC': data.pf18_alc == null ? '' : data.pf18_alc,
            'PF 19%': data.pf19 == null ? '' : data.pf19,
            'PF 20%': data.pf20 == null ? '' : data.pf20,
            'PF 21%': data.pf21 == null ? '' : data.pf21,
            'PF 22%': data.pf22 == null ? '' : data.pf22,
            'PMVG SEM IMPOSTO': data.pmvg_sem_imposto == null ? '' : data.pmvg_sem_imposto,
            'PMVG 0%': data.pmvg0 == null ? '' : data.pmvg0,
            'PMVG 12%': data.pmvg12 == null ? '' : data.pmvg12,
            'PMVG 17%': data.pmvg17 == null ? '' : data.pmvg17,
            'PMVG 17% ALC': data.pmvg17_alc == null ? '' : data.pmvg17_alc,
            'PMVG 17.5%': data.pmvg17_5 == null ? '' : data.pmvg17_5,
            'PMVG 17.5% ALC': data.pmvg17_5_alc == null ? '' :  data.pmvg17_5_alc,
            'PMVG 18%': data.pmvg18 == null ? '' : data.pmvg18,
            'PMVG 18% ALC': data.pmvg18_alc == null ? '' : data.pmvg18_alc,
            'PMVG 19%': data.pmvg19 == null ? '' : data.pmvg19,
            'PMVG 20%': data.pmvg20 == null ? '' : data.pmvg20,
            'PMVG 21%': data.pmvg21 == null ? '' : data.pmvg21,
            'PMVG 22%': data.pmvg22 == null ? '' : data.pmvg22,
            'RESTRIÇÃO HOSPITALAR': data.restricao_hospitalar ? 'Sim': 'Não',
            'CAP': data.CAP ? 'Sim' : 'Não',
            'CONFAZ 87': data.confaz87 ? 'Sim': 'Não',
            'ICMS 0%': data.icms0 ? 'Sim': 'Não',
            'ANÁLISE RECURSAL': data.analise_recursal == 'nan' ? '' : analise_recursal,
            'LISTA CONCESSÃO CRÉDITO (PIS/COFINS)': {'P': 'Positiva', 'N': 'Negativa'}[data.lista_concessao_credito],
            'COMERCIALIZAÇÃO 2022': data.comercializacao_2022 ? 'Sim' : 'Não',
            'TARJA': data.tarja
        });
    });

    var ws = utils.json_to_sheet(rows);
    var wb = utils.book_new();
    utils.book_append_sheet(wb, ws, 'PMVG'),
    writeFile(wb, name.value + '.xlsx', {compression: true});

}

const markforexport = (id) => {
    let element = document.getElementById('check' + id);
    console.log(element.checked);

    if(element.checked) lines_to_import.push(id);
    else lines_to_import = lines_to_import.filter(v => v != id)
}

const top = () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    })
}

const markallforexport = () => {
    const value = document.getElementById("maincheck").checked;

    data.map((d) => {
        let id = 'check' + d.id;
        let element = document.getElementById(id);
        element.checked = value;
        markforexport(d.id);
    });
}
</script>

<template>
    <div class="row justify-content-start">
        <div class="col-6">
            <ul class="ul">
                <li class="li text-dark">Marque o checkbox de cada linha deseja a ser exportada</li>
                <li class="li text-dark">Clique em uma coluna para ver seu conteúdo completo no detalhamento</li>
                <li class="li-text-dark">Marque o checkbox do cabeçalho para marcar todos os registros</li>
            </ul>
        </div>
        <div class="col-6">
            <strong>DETALHAMENTO:</strong>
            <textarea  class="textarea form-control" id="detalhamento">
                     {{  detail  == null ? '' : detail }}
            </textarea>
        </div>
    </div>

    <div class="row justify-content-start" style="margin-top: 30px">
        <div class="col-6">
            <input class="form-control" v-model="filename" placeholder="Nome do Arquivo a ser Exportado (sem o .xls)">
        </div>
        <div class="col-6">
            <button class="btn btn-success text-center" @click="filexport()">Exportar</button>
        </div>
    </div>

    <div v-if="show" class="row justify-content-start rowform">
        <div class="col-12">
            <table class="table">
                <thead class="table-info">
                    <tr>
                        <th><input id="maincheck" class="form-check-input" type="checkbox" @change="markallforexport()"></th>
                        <th>PRINCIPIO ATIVO</th>
                        <th>CNPJ</th>
                        <th>LABORATÓRIO</th>
                        <th>GGREM</th>
                        <th>REGISTRO</th>
                        <th>EAN 1</th>
                        <th>EAN 2</th>
                        <th>EAN 3</th>
                        <th>PRODUTO</th>
                        <th>APRESENTAÇÃO</th>
                        <th>CLASSE TERAPÊUTICA</th>
                        <th>TIPO PRODUTO</th>
                        <th>REGIME PREÇO</th>
                        <th>PF SEM IMPOSTO</th>
                        <th>PF 0%</th>
                        <th>PF 12%</th>
                        <th>PF 17%</th>
                        <th>PF 17% ALC</th>
                        <th>PF 17.5%</th>
                        <th>PF 17.5% ALC</th>
                        <th>PF 18%</th>
                        <th>PF 18% ALC</th>
                        <th>PF 19%</th>
                        <th>PF 20%</th>
                        <th>PF 21%</th>
                        <th>PF 22%</th>
                        <th>PMVG SEM IMPOSTO</th>
                        <th>PMVG 0%</th>
                        <th>PMVG 12%</th>
                        <th>PMVG 17%</th>
                        <th>PMVG 17% ALC</th>
                        <th>PMVG 17,5%</th>
                        <th>PMVG 17.5% ALC</th>
                        <th>PMVG 18%</th>
                        <th>PMVG 18% ALC</th>
                        <th>PMVG 19%</th>
                        <th>PMVG 20%</th>
                        <th>PMVG 21%</th>
                        <th>PMVG 22%</th>
                        <th>RESTRIÇÃO HOSPITALAR</th>
                        <th>CAP</th>
                        <th>CONFAZ 87</th>
                        <th>ICMS 0%</th>
                        <th>ANÁLISE RECURSAL</th>
                        <th>LISTA CONCESSÃO CRÉDITO (PIS/COFINS)</th>
                        <th>COMERCIALIZAÇÃO</th>
                        <th>TARJA</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="data.length == 0">
                        <td colspan="48" class="text-start"><strong>Nenhuma informação encontrada</strong></td>
                    </tr>
                    <tr v-else v-for="d in data" :key="d.id">
                        <td><input :id="'check' + d.id" class="form-check-input" type="checkbox" @change="markforexport(d.id)"></td>
                        <td><input class="form-control" type="text" :value="d.principio_ativo" readonly @click="detail=d.principio_ativo; top()"></td>
                        <td><input class="form-control" type="text" :value="d.cnpj" readonly @click="detail=d.cnpj; top()"></td>
                        <td><input class="form-control" type="text" :value="d.laboratorio" readonly @click="detail=d.laboratorio; top()"></td>
                        <td><input class="form-control" type="text" :value="d.codigo_ggrem" readonly @click="detail=d.codigo_ggrem; top()"></td>
                        <td><input class="form-control" type="text" :value="d.registro" readonly @click="detail=d.registro; top()"></td>
                        <td><input class="form-control" type="text" :value="d.ean1" readonly @click="detail=d.ean1; top()"></td>
                        <td><input class="form-control" type="text" :value="d.ean2" readonly @click="detail=d.ean2; top()"></td>
                        <td><input class="form-control" type="text" :value="d.ean3" readonly @click="detail=d.ean3; top()"></td>
                        <td><input class="form-control" type="text" :value="d.produto" readonly @click="detail=d.produto; top()"></td>
                        <td><input class="form-control" type="text" :value="d.apresentacao" readonly @click="detail=d.apresentacao; top()"></td>
                        <td><input class="form-control" type="text" :value="d.classe_terapeutica" readonly @click="detail=d.classe_terapeutica; top()"></td>
                        <td><input class="form-control" type="text" :value="d.tipo_produto" readonly @click="detail=d.produto; top()"></td>
                        <td><input class="form-control" type="text" :value="d.regime_preco" readonly @click="detail=d.regime_preco; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf_sem" readonly @click="detail=d.pf_sem; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf0" readonly @click="detail = d.pf0; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf12" readonly @click="detail = d.pf12; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf17" readonly @click="detail = d.pf17;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf17_alc" readonly @click="detail = d.pf17_alc;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf17_5" readonly @click="detail = d.pf17_5;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf17_5_alc" readonly @click="detail = d.pf17_5_alc;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf18" readonly @click="detail = d.pf18;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf18_alc" readonly @click="detail = d.pf18_alc;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf19" readonly @click="detail = d.pf19;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf20" readonly @click="detail = d.pf20;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf21" readonly @click="detail = d.pf21;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pf22" readonly @click="detail = d.pf22;top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg_sem_imposto" readonly @click="detail = d.pmvg_sem_imposto; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg0" readonly @click="detail = d.pmvg0; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg12" readonly @click="detail = d.pmvg12; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg17" readonly @click="detail = d.pmvg17; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg17_alc" readonly @click="detail = d.pmvg17_alc; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg17_5" readonly @click="detail = d.pmvg17_5; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg17_5_alc" readonly @click="detail = d.pmvg17_5_alc; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg18" readonly @click="detail = d.pmvg18; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg18_alc" readonly @click="detail = d.pmvg18_alc; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg19" readonly @click="detail = d.pmvg19; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg20" readonly @click="detail = d.pmvg20; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg21" readonly @click="detail = d.pmvg21; top()"></td>
                        <td><input class="form-control" type="text" :value="d.pmvg22" readonly @click="detail = d.pmvg22; top()"></td>
                        <td><input class="form-control" type="text" :value="d.restricao_hospitalar ? 'Sim' : 'Não'" readonly @click="detail = d.restricao_hospitalar ? 'Sim' : 'Não'; top();"></td>
                        <td><input class="form-control" type="text" :value="d.CAP ? 'Sim' : 'Não'" readonly @click="detail = d.CAP ? 'Sim' : 'Não'; top();"></td>
                        <td><input class="form-control" type="text" :value="d.confaz87 ? 'Sim' : 'Não'" readonly @click="detail = d.confaz87 ? 'Sim' : 'Não'; top()"></td>
                        <td><input class="form-control" type="text" :value="d.icms0 ? 'Sim' : 'Não'" readonly @click="detail = d.icms0 ? 'Sim' : 'Não'; top()"></td>
                        <td><input class="form-control" type="text" :value="d.analise_recursal == 'nan' ? '': d.analise_recursal" readonly @click="detail=d.analise_recursal == 'nan' ? '' : d.analise_recursal; top()"></td>
                        <td><input class="form-control" type="text" :value="{'P' : 'Positiva', 'N': 'Negativa'}[d.lista_concessao_credito]" readonly @click="detail = {'P': 'Positiva', 'N': 'Negativa'}[d.lista_concessao_credito]; top()"></td>
                        <td><input class="form-control" type="text" :value="d.comercializacao_2022 ? 'Sim' : 'Não'" readonly @click="detail = d.comercializacao_2022 ? 'Sim' : 'Não'; top();"></td>
                        <td><input class="form-control" type="text" :value="d.tarja" readonly @click="detail = d.tarja; top()"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="row justify-content-start">
        <div class="col-4">
            <p class="text-dark"><strong>Registros achados {{ data.length }}</strong></p>
        </div>
    </div>
</template>


<style scoped>

table tr th {
    font-size: 12px !important;
    min-width: 120px !important;
    text-align: center;
}

table thead {
    background-color: #0dcaf0 !important;
}

.rowform {
    margin-top: 30px;
}

.maincheck {
    width: 25px;;
}

.btn {
    width: 100% !important;
}

</style>