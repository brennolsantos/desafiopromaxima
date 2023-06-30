from django.core.management import BaseCommand
from django.core.management.base import CommandParser
import pandas as pd
from core.models import MedPMGV 
import math 
import decimal

def get_str(s):
    return s if s is not None and s != float('nan') else ''

def get_float(s):

    if str(s).strip() == 'nan':
        return None

    s =  float(s.replace(',', '.') if type(s) == str else s) if s is not None and s != '' else None 

    return s

def get_boolean(s):
    choices = {
        'Sim': True,
        'Não': False 
    }

    return choices[s] if s.strip() in choices.keys() else None

def get_pn(s):
    choices = {
        'Positiva': 'P',
        'Negativa': 'N'
    }

    if s is not None and s != '':
        return choices[s] if s in choices.keys() else None

    return None

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('xls', nargs=1, type=str)

    def handle(self, *args, **options):
        fname = options['xls'][0]
        sheet = pd.read_excel(fname)

        start_line = 0 
        finish_column = 'Unnamed: 46'

        flist = sheet['Secretaria Executiva - CMED'].tolist()

        for f in flist:
            if f == 'PRINCÍPIO ATIVO':
                start_line += 1
                break 

            start_line += 1

        columns = sheet.columns.ravel()
        index_col = 0
        index_line = 0
        list_values = []
        
        #comment esse for e descomente o comentário seguinte caso queira
        #buscar todos os dados do xlsx
        for i in range(len(flist[start_line:start_line + 200])):
            list_values.append([])

        # for i in range(len(flist[start_line:])):
        #     list_values.append([])

        index_col = 0 

        objects = []

        while index_line < len(list_values):
            print(f'Current line: {index_line + 1}')
            for index_col in range(len(columns)):
                col = columns[index_col]
                value = sheet[col].to_list()[start_line + index_line]
                value = '' if value == 'nan' else value
                list_values[index_line].append(value)
                index_col += 1

            lobj = list_values[index_line]

            pmvg = MedPMGV(principio_ativo = get_str(lobj[0]),
                cnpj = get_str(lobj[1]),
                laboratorio = get_str(lobj[2]),
                codigo_ggrem = get_str(lobj[3]),
                registro = get_str(lobj[4]),
                ean1 = get_str(lobj[5]),
                ean2 = get_str(lobj[6]),
                ean3 = get_str(lobj[7]),
                produto = get_str(lobj[8]),
                apresentacao = get_str(lobj[9]),
                classe_terapeutica = get_str(lobj[10]),
                tipo_produto = get_str(lobj[11]),
                regime_preco = get_str(lobj[12]),
                pf_sem = get_float(lobj[13]),
                pf0 = get_float(lobj[14]),
                pf12 = get_float(lobj[15]),
                pf17 = get_float(lobj[16]),
                pf17_alc = get_float(lobj[17]),
                pf17_5 = get_float(lobj[18]),
                pf17_5_alc = get_float(lobj[19]),
                pf18 = get_float(lobj[20]),
                pf18_alc = get_float(lobj[21]),
                pf19 = get_float(lobj[22]),
                pf20 = get_float(lobj[23]),
                pf21 = get_float(lobj[24]),
                pf22 = get_float(lobj[25]),
                pmvg_sem_imposto = get_float(lobj[26]),
                pmvg0 = get_float(lobj[27]),
                pmvg12 = get_float(lobj[28]),
                pmvg17 = get_float(lobj[29]),
                pmvg17_alc = get_float(lobj[30]),
                pmvg17_5 = get_float(lobj[31]),
                pmvg17_5_alc = get_float(lobj[32]),
                pmvg18 = get_float(lobj[33]),
                pmvg18_alc = get_float(lobj[34]),
                pmvg19 = get_float(lobj[35]),
                pmvg20 = get_float(lobj[36]),
                pmvg21 = get_float(lobj[37]),
                pmvg22 = get_float(lobj[38]),
                restricao_hospitalar = get_boolean(lobj[39]),
                CAP = get_boolean(lobj[40]),
                confaz87 = get_boolean(lobj[41]),
                icms0 = get_boolean(lobj[42]),
                analise_recursal = get_str(lobj[43]),
                lista_concessao_credito = get_pn(lobj[44]),
                comercializacao_2022 = get_boolean(lobj[45]),
                tarja = get_str(lobj[46])
             )

            objects.append(pmvg)

            index_line += 1
            index_col = 0

        MedPMGV.objects.bulk_create(objects)
        print(f'{MedPMGV.objects.all().count()} registros criados')





