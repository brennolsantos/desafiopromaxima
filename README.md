# desafiopromaxima
Projeto do desafio para promaxima

Esse projeto consiste em uma aplicação frontend Nuxtjs integrada com uma API RESTful em Django com dados persistidos em um banco PostgreSQL. Os dados são importados da seguinte fonte: https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos 
A importação ocorre via comando personalizado no backend com o arquivo .xlsx já incluido no repositório (uma possivel melhoria poderia ser o fetching automatico desse arquivo no back pela url). A tela (imagens mais a frente ainda nessa documentação) consiste em uma entrada de filtro e chave de busca.

Os filtros disponíveis estão listados a seguir e não precisam ser digitados, pois estão em uma tag de seleção. As chaves de busca pode ser uma string incompleta ou completa do dado procurado que está no campo do xls indicado pelo filtro.

- PRINCÍPIO ATIVO
- CNPJ
- LABORATÓRIO
- CÓDIGO GGREM
- REGISTRO EAN
- PRODUTO
- APRESENTAÇÃO
- CLASSE TERAPÊUTICA
- TIPO DE PRODUTO (STATUS DO PRODUTO)
- REGIME DE PREÇO
- RESTRIÇÃO HOSPITALAR
- CAP
- CONFAZ 87
- ICMS 0%
- LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFIN
- COMERCIALIZAÇÃO 2022
- TARJA

Após uma busca bem sucedida (caracteres inválidos ou totalmente em branco podem retornar nenhum dado ou, em casos especificos um Response 404, por isso certifique-se de digitar um valor e escolher um filtro. Atente-se a tipo de campo. Os campos "restrição hospitalar", "cap", "confaz 87", "icms" e "comercialização 2022" devem receber como entrada na buscas as palavras "sim" ou "não" podendo começar com uma letra maiúscula. O campo "lista de concessão de crédito" consulta da mesma forma apenas com "positiva" e "negativa". fica como melhoria usar selects de opções padrões nesses campos, o que não foi possível ainda devido ao pouco tempo livre de desenvolvimento.
No caso do campo for uma informacao numérica ou um texto (presumi que o usuário sabe o que significa esses nomes), não ha restrição de caracteres ou palavras.

A tela seguinte (também tera imagens). Consiste de uma tabela com todos os registros encontrados. Se não houve resultados ou algum erro na requisição, a tabela estara vazia. A caixa de texto no inicio de tela serve para exibir o texto completo de uma coluna que possui texto muito longo para a tabela. Apenas clique no campo e a informação aparecerá na caixa. Isso funciona para a tabela toda. 

Você pode selecionar linhas para serem exportadas em xls. A primeira coluna contem um checkbox e um checkbox no cabeçalho da tela marca ou desmarca todas as linhas.

O input de formatação aceita um nome para o arquivo. Não precisa colocar a extensão. Aperte o botão de importação e o download do arquivo acontecerá.

URLS inválidas apontam para a tela de erra padrão do Nuxt.

# INSTALAÇÃO DA APLICAÇÃO NA MÁQUINA

Certifique-se de ter o Docker,  Docker-compose e git instalados na máquina. No seu computador, vá para o diretorio desejado (o meu foi C:\tutorial). Abra este diretorio no prompt e dê um git clone neste repositório. 

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/1d4af34b-6820-48cd-9e81-661a37d70fcc)

Em seguida, mude para o diretorio criado e vá para o arquivo "backend\core\managements\commands\insert_from_xls.py". Neste arquivo há um unico comentário que orienta se você não faz nenhuma modificação e importa apenas 200 linhas do .xlsx ou importa todas para a banco. Importar todas as linhas leva alguns minutos devido a extensão do arquivo 
![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/cdc3afb6-9f5e-43c5-b1e0-63e86ad9e751)


Agora vamos criar os containers: posicione-se na mesma pasta do docker-compose.yml e rode no promtpt: "docker-compose build".
Aguarde até a criação de todos os containeres.

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/c4d395e9-4dd7-4914-a2c4-cc4141c46059)


Antes de usar a aplicação vamos ter que criar a tabela usada pelo django e importar os arquivos.

Já podemos subir com: docker-compose up -d
Verifique se a aplicação em localhost:3000 funcionou, pois nem sempre o vue-router é instalado automaticamente. Se isso acontecer:

&nbsp;


* Execute "docker-compose exec frontend npm install vue-router"

&nbsp;

 
e dê build novamente.

* Execute no prompt: docker-compose exec python manage.py makemigrations

&nbsp;


E em seguida: docker-compose exec python manage.py migrate

&nbsp;


Verifique no log se alguma tabela do app "core" foi criada. Caso não:

&nbsp;
* Execute no prompt: docker-compose exec python manage.py makemigrations core

&nbsp;

E em seguida: docker-compose exec python manage.py migrate

&nbsp;


Agora já podemos importar dados do nosso xlsl.

&nbsp;


* Execute no prompt: docker-compose exec backend python manage.py insert_from_xls import.xls
  
&nbsp;


Acompanhe o número de registros incluídos e, ao fim, não esqueça de levantar a api novamente com:

&nbsp;


* Execute: docker-compose exec backend python manage.py runserver 0.0.0.0:8080

  
&nbsp;


# Usando a aplicação

API: http://localhost:8080
APP: http://localhost:3000

Estamos na tela inicial: 

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/cb23819c-383c-49d1-82ea-88d8fdd2daa5)

Vamos tentar achar registros com principio ativo Valproato:
![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/c592abb6-1844-43ac-8592-3f30d603015f)

Foi achado o seguinte registro para nossa importação de 200 registros
![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/b828b5a9-f657-4b30-9704-04a47e900a6d)

A tabela tem uma linha extensa, mas podemos dar scroll para ver os campos restantes, e caso a informação for longa demais para a coluna você pode dar um clique na coluna e será levada a informação completa pela caixa de detalhamento.

Vamos tentar exportar esse registro. Marque o checkbox do cabecalho ou da linha do registro

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/4fc8dc1c-020f-4c5b-8d59-22e3d437aae3)

Agora, dê um nome simples ao arquivo e aperte em exportar

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/6ee3c176-0ce3-4584-9577-e0e304626bfb)

Foi feito o Download automático do arquivo com  a extensão. E você já pode conferir os dados no excel.

![image](https://github.com/brennolsantos/desafiopromaxima/assets/75213610/325e871b-abbd-4d33-afcd-4f5daf670058)



# Considerações

Tive de programar esse sistema nas poucas horas livres que a ocupação integral me permite, mas busquei ao máximo deixar bem feito e conciso.

Espero que tenham gostado.




