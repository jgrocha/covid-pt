# Projeto Final - Covid-19
# Análises Estátisticas e Mapeamento de Dados

COVID-19 é o nome, atribuído pela Organização Mundial da Saúde, à doença provocada pelo novo coronavírus SARS-COV-2, que pode causar infeção respiratória grave como a pneumonia. Este vírus foi identificado pela primeira vez em humanos, no final de 2019, na cidade chinesa de Wuhan, província de Hubei, tendo sido confirmados casos em outros países.
De modo a avaliar todas as competências lecionadas na UC de Sistemas de Informação Geograficos, foi realizado um projeto que se foca em análises estátisicas desta doença Mundialmente e em dois países, Portugal e Espanha.

- São apresentadas 4 pastas neste repositório:

Pasta | Conteúdo
------------ | -------------
[Data](https://github.com/CarinaA81247/Epidemiologia/tree/master/Data) | Contém todos os datasets usados nos notebooks.
[Exercícios](https://github.com/CarinaA81247/Epidemiologia/tree/master/Exercic%C3%ADos) | Contém todos os exercícios iniciais da UC.
[Geopackges e Shapes](https://github.com/CarinaA81247/Epidemiologia/tree/master/Geopackges%20e%20shapes) | Contém todos geopackges usados para realização de mapas nos notebooks e as shapes que foram utilizadas.
[Figuras](https://github.com/CarinaA81247/Epidemiologia/tree/master/Figuras) | Contém todas as figuras utilizadas nesta página.
[Notebooks](https://github.com/CarinaA81247/Epidemiologia/tree/master/Notebooks) | Contém todos os nootebooks elaborados.

- Foram elaborados 6 notebooks:

🗂️[Covid-19_EspanhaGráficos.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Covid-19_EspanhaGr%C3%A1ficos.ipynb) - Onde são apresentadas algumas estatísticas por comunidades autónomas de Espanha.

🗂️[Covid-19_Portugal.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Covid-19_Portugal.ipynb) - Onde são apresentadas algumas estatisticas relativas aos dados de Portugal.

🗂️[Espanha_curvas_logisticas_gaussianas.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Espanha_curvas_logisticas_gaussianas.ipynb) - Onde são apresentadadas curvas logísticas e gaussianas ajustadas aos dados de Espanha.

🗂️[Estatisticas_mundiais_espanha.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Estatisticas_mundiais_espanha.ipynb) - Aqui são apresentadas estatísticas relativas a dados mundiais e mais específicas apenas relativas a Espanha.

🗂️[Global_map.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Global_map.ipynb) - Neste notebook foram elaborados alguns mapas mundo com alguns dados relativos à doença.

🗂️[Mapas_Espanha.ipynb](https://github.com/CarinaA81247/Epidemiologia/blob/master/Notebooks/Mapas_Espanha.ipynb) - Aqui foram elaborados mapas de Espanha.

## Análise das estatísticas mundiais

- Inicialmente é apresentado um mapa mundo com os casos confirmados até ao dia 31-05-2020. Este mapa, assim como outros, foi elaborado no Qgis e importado com um Geopackge para o Jupyter notebook.

![Mapa Mundo com casos confirmados](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/global_map_confirmed.png)

- Foram estruturados alguns gráficos com estatísticas relativas aos 10 países com mais casos confirmados e mais mortes.

![10 países com mais casos confirmados](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/10_countrie_global_confirmed.png) ![10 países com mais mortes](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/10_countrie_global_death.png)

- Uma vez que esta doença pode causar infeção respiratória grave ou pneumonia, sabe-se que pessoas que têm hábito de fumar são pessoas que podem estar em risco. Desta forma, foram criados gráficos com os 10 países com elevada percentagem de mulheres fumadoras e homens fumadores. Assim como outras características relacionadas com a covid-19 também foram representadas. A título de exemplo, é apresentado a seguir o gráfico com os 10 países com maiores percentagens de mulheres fumadoras.

**Gráfico dos 10 países com maiores percentagens de mulheres fumadoras**

![Mulheres Fumadoras](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/10_countrie_global_female_smokers.png)

## Espanha

- Foram analisados também os dados relativos a Espanha. Apresentando-se aqui alguns desses gráficos também.

**Gráfico do Total de mortes por dia na Espanha**

![Mortes Espanha](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/sapin_total_deaths.png)

**Gráfico dos casos confirmados por comunidades Autónomas da Espanha**

![Casos por CCAA](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/spain_cases_ccaa.png)

- Os dados de Espanha relativamente aos casos confirmados foram ajustados a uma curva logística de modo a prever os próximos dias. No mesmo nootebook é possível encontrar curvas logísticas ajustadas a outros dados e também curvas gaussianas.

**Curva Logística**

![Curva Logística](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/spain_logistic_curve.png)

**Curva Gaussiana**

![Cuva Gaussiana](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/spain_gaussiana.png)

- Relativamente a Espanha foram também criados alguns mapas, como o que se pode ver na próxima figura.

**Mapa de Espanha com o total de casos confirmados**

![Mapa de casos confirmados](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/map_spain_casos_confirmados.png)

**Mapa de Espanha com os novos casos para o dia 24-05-2020**

![Mapa de novos casos Espanha](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/map_spain_casos_novos.png)

## Portugal

- Por fim, foram avaliados dados da doença em Portugal, estes dados foram lidos da base de dados em vez de lidos em documentos csv como os dados anteriores. Como exemplo de um dos gráficos feitos, pode observar-se a seguir o Número de Casos Confirmados por distrito.

**Gráfico de casos confirmados por Distrito**

![Casos Distrito](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/portugal_casos_distrito.png)

- A partir de um geopackeg também recolhido da mesma fonte de dados, foi importado a camada referente ao mapa de Portugal com os casos confirmados por distrito.

**Mapa de Portugal com casos confirmados por Distrito**

![Mapa Portugal Distritos](https://github.com/CarinaA81247/Epidemiologia/blob/master/Figuras/map_portugal_casos_distrito.png)

- Em conclusão, apenas referir que outras abordagens gráficas e elaboração de mapas são evidenciadas nos notebooks.

## Webgrafia

- Todas as fontes de dados são apresentadas em cada notebook individualmente.

## Trabalho Realizado por:

Carina Gonçalves A81247 

Mestrado Integrado em Engenharia Biomédica - Ramo de Informática Médica

UC - Sistemas de Informação Geográficos 2019/2020

## Data:

02-06-2020



