# *Projeto Final da aluna Cláudia Alves (A80790) para a UC de Sistemas de Informação Geográfica*

Visualização de casos de COVID-19 através de gráficos e mapas

Neste notebook estão alguns gráficos relativos aos casos de COVID-19 em alguns países

##### Os datasets utilizados foram retirados dos seguintes repositórios do GitHub

* https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

* https://github.com/open-covid-19/data


##### O repositório encontra-se dividido em diferentes pastas:
* **[COVID](https://github.com/Claudia-Alves/Epidemiologia/tree/master/Projeto%20Final%20-%20A80790/COVID)**: Dados usados na obtenção dos mapas;
* **[Dados](https://github.com/Claudia-Alves/Epidemiologia/tree/master/Projeto%20Final%20-%20A80790/Dados)**: Dados usados nas restantes estatísticas, incluindo os novos ficheiros criados;
* **[Figuras](https://github.com/Claudia-Alves/Epidemiologia/tree/master/Projeto%20Final%20-%20A80790/Figuras)**: Imagens dos gráficos, estatísticas e mapas;
* **[Países](https://github.com/Claudia-Alves/Epidemiologia/tree/master/Projeto%20Final%20-%20A80790/Paises)**: Utilizado para a realização dos mapas;
* O **notebook** é o ficheiro [Projeto_Final.ypnb](https://github.com/Claudia-Alves/Epidemiologia/blob/master/Projeto%20Final%20-%20A80790/Projeto_final.ipynb).

## Agrupamento dos dados por países

Obtiveram-se alguns gráficos com os casos por países, utilizou-se uma função para apenas contar os países com *mais de 100* casos.
__*NOTA*: em alguns gráficos, como os valores são muito elevados, aparece a notação científica.__


<p align="center">
 <img src="Figuras/Paises_pie.png" width="750"> 
</p>

Gráfico com os confirmados e os mortos, de acordo com os países com mais confirmados.
<p align="center">
<img src="Figuras/Paises_BarraH.png"  width="750">
</p>

Em ambos os gráficos, é possível verificar que o país com mais casos é os Estados Unidos da América, seguido de Itália, Espanha e França.


Gráficos com o total de confirmados vs mortos, para tal fez-se a soma de todos os confirmados e mortos por país até a data.

<p align="center">
<img src="Figuras/Confirmados_mortos_pie.png"  width="500">
</p>

![Confirmados vs mortos](Figuras/Total_Confirmados.png)

### Casos por categoria

Tendo em conta alguns dados de tempo médio até ser dada a alta a casos graves e críticos, obteve-se um gráfico com o Tempo médio de hospitalização para cada um deles. Observando a reta, dá aproximadamente um tempo médio de hospitalização 12 dias para casos graves e de 15 dias para casos hospitalizados.

<p align="center">
<img src="Figuras/TempoHospitalizacao.png" width="600"> 
</p>

Fez-se um gráfico relativo aos casos de COVID-19 por três categorias, leves, graves e críticos. 
Observando-o, verifica-se que, felizmente, a maioria dos casos são casos leves.

<p align="center">
<img src="Figuras/CasosLevesGravesCriticos.png" width="500">
</p>


## Mapas mundo

Utilizaram-se os dados atuais de mortos e recuperados nos diferentes países para construir os mapas com a Taxa de Mortalidade no Mundo e com a Taxa de Recuperação no mundo. 

#### Taxa de Mortalidade 
   

![TaxaMortalidade](Figuras/TaxaMortalidadeMundo.png)

Verifica-se que a Austrália e a Etiópia são dois dos países com menor taxa de mortalidade devido ao COVID-19.

#### Taxa de Recuperação 

![TaxaRecuperados](Figuras/TaxaRecuperadosMundo.png)

De notar, que a Austrália é um dos países com maior taxa de recuperação e menor taxa de mortalidade.


## Estatísticas de países ou regiões com mais casos

Para estas estatísticas de países ou regiões com mais casos fizeram-se alterações ao dataset utilizado, incluindo selecionar algumas colunas, agregar os dados, fazer somas e guardar esses dados em novos ficheiros csv que posteriormente foram abertos e ordenados de modo a escolher o top 10. Estes ficheiros podem ser encontrados na pasta Dados.

### Top 10 países 

#### Com mais casos confirmados

<p align="center">
 <img src="Figuras/Top10paisesCasos.png" width="500"> 
</p>

#### Com mais mortos

<p align="center">
 <img src="Figuras/Top10paisesMortes.png" width="500"> 
</p>

#### Com mais recuperados
<p align="center">
 <img src="Figuras/Top10paisesRecuperados.png" width="500"> 
</p>

#### Com mais casos hospitalizados

<p align="center">
 <img src="Figuras/Top10paisesHospitalizados.png" width="500"> 
</p>

#### Com mais casos nos cuidados intensivos

<p align="center">
 <img src="Figuras/Top10paisesNosUCI.png" width="500"> 
</p>

#### Com mais testes
<p align="center">
 <img src="Figuras/Top10paisesTestes.png" width="500"> 
</p>

### Top regiões na Austrália

#### Regiões com mais casos confirmados
<p align="center">
 <img src="Figuras/TopRegioesAustraliaCasos.png" width="500"> 
</p>


#### Regiões com mais recuperados
<p align="center">
 <img src="Figuras/TopRegioesAustraliaRecuperados.png" width="500"> 
</p>


#### Regiões com mais mortos
<p align="center">
 <img src="Figuras/TopRegioesAustraliaMortos.png" width="500"> 
</p>

#### Regiões com mais testes
<p align="center">
 <img src="Figuras/TopRegioesAustraliaTestados.png" width="500"> 
</p>

#### Regiões com mais casos hospitalizados
<p align="center">
 <img src="Figuras/TopRegioesAustraliaHospitalizados.png" width="500"> 
</p>


## Casos em Espanha

Total de confirmados e mortos em Espanha por data.

![Espanha](Figuras/Espanha_total.png)

### Casos numa região de Espanha

Gráfico com os confirmados e mortos para as Asturias, uma das sub-regiões de Espanha, até a data mais atual, de notar que os dados para as sub-regiões não são tão atuais como os dados no país todo, ou seja, enquanto que para Espanha no geral se obteve os dados até ao dia 30 de Maio, para a sub-região o mais recente é 21 de maio.

![Asturias](Figuras/AsturiasConfirmados.png)


## Casos em Itália

### Total de casos Confirmados e Mortos 

![Itália](Figuras/Italia_total.png)

### Heurística - modelagem exponencial

Fez-se uso de uma heurística já existente e a encontrada é do dia **17 de março**, portanto,  os gráficos seguintes são baseados nessa data.

![ItáliaH](Figuras/Italia_heuristica.png)

### Estimativa de 3 dias vs dados reais

![ItáliaEst](Figuras/ItaliaEstimativa3dias.png)

### Estimar 3 dias futuros

![ItáliaFut](Figuras/ItaliaFuturo3dias.png)


## Casos na Corea do Sul

![CoreaS](Figuras/CoreaSulTotal.png)

### Heurística - modelagem exponencial

Fez-se uso de uma heurística já existente e a encontrada é do dia **18 de março**, portanto,  os gráficos seguintes são baseados nessa data.

![CoreaSH](Figuras/CoreaSHeuristicaGomperstz.png)


### Estimativa de 3 dias vs dados reais

![CoreaSEst](Figuras/CoreaSEstimativa.png)

### Estimar 3 dias futuros

![CoreaSFut](Figuras/CoreaSFuturo3Dias.png)



