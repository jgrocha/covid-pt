# SIG - Final Project 

## Motivação:
No âmbito da Unidade Curricular de Sistema de Informação Geográfica foi solicitado um projeto que envolvesse a manipulação e tratamento de dados relacionados com o vírus COVID-19. No presente trabalho foram tratados e manipulados dados nas ferramentas QGIS e Jupyter (PyQGIS) e também realizada a extração de dados provindas de bases de dados.

Abaixo segue-se a estruturação do trabalho, bem como o que cada parte inclui.


## Organização da pasta:
  * [Countries](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Countries): layers utilizadas para criar os mapa mundo;
  * [Covid19](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Covid19): dados relativos à doença, retirados do repositório [COVID-19](https://github.com/CSSEGISandData/COVID-19);
  * [Figures](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Figures): imagens relativas a Portugal [(pasta Portugal)](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Figures/Portugal) e ao Mundo [(pasta WW)](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Figures/WW);
  * [Geopackages](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Geopackages): dados relativos a Portugal do repositório [covid-pt](https://github.com/jgrocha/covid-pt);
  * [FinalProject-PT.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-PT.ipynb);
  * [FinalProject-WW_maps.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-WW_maps.ipynb)
  * [FinalProject-WW_stats.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-WW_stats.ipynb)
  


## Organização da informação (ficheiro ipynb): 

**NOTA**: Todas as imagens têm hiperligação para a pasta onde estão alocadas, basta clicar em cima delas.

### [FinalProject-PT.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-PT.ipynb):

* Construção de mapas por concelho (lado esquerdo) e por distrito (lado direito) dos casos em Portugal:
 ![Concelho](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/Portugal/MapaPortugalConcelhos.png)
 ![Distrito](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/Portugal/MapaPortugalDistritos.png)

* Construção de gráficos barras, circulares com e sem legenda das localidades com mais de 500 casos, quer para concelhos como para os distritos. De seguida, apresentam-se os dos concelhos:
![Bar Chart](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/Portugal/barConcelho500.png)
![Pie Chart](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/Portugal/pieConcelho500.png)
![Pie Chart legend](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/Portugal/pie_legConcelho500.png)


Relativamente à informação mundial foram estudados os casos de confirmados, ativos (confirmados-mortos-recuperados), mortos e recuperados por meio de mapas e gráficos estatísticos.


### [FinalProject-WW_maps.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-WW_maps.ipynb):

* Mapa Taxa Mortalidade:
![Mapa Taxa Mortalidade](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Mortalidade.png)

* Mapa Taxa Recuperados:
![Mapa Taxa Recuperados](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Recuperados.png)

* Mapa Taxa Recuperados por morte: 
![Mapa Taxa Recuperados por morte](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Recuperados_morte.png)


### [FinalProject-WW_stats.ipynb](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-WW_stats.ipynb):

* Top 10 países com casos confirmados: 
![Casos Confirmados](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Top10Countries(ConfirmedCases).png)

* Top 10 países com casos de mortes:
![Casos de Mortes](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Top10Countries(DeathsCases).png)

* Top 10 países com casos recuperados:
![Casos Recuperados](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Top10Countries(RecoveredCases).png)

* Top 10 países com casos ativos (sendo estes os casos respetivos às pessoas que estão infetadas, mas ainda não morreram nem estão recuperadas):
![Casos Ativos](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/Top10Countries(ActiveCases).png)

* Gráficos e mapas não estáticos que por questões de renderização, devem ser vizualizados no [nbviewer](https://nbviewer.jupyter.org/github/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/FinalProject-WW_stats.ipynb);

* Gráfico comparativo entre 3 países (neste caso foram escolhidos: Portugal, China e Itália):
![Gráfico comparativo](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/3Countries.png)

* Gráfico de todos os países que apresentam um total de mais de 10000 casos:
![casos](https://github.com/BM-a81824/Epidemiologia/blob/master/SIG-FinalProject/Figures/WW/WW10000.png)

* Curve Fitting de todos os países, uma vez que são bastantes, vizualizar as imagens CurveFitting_(...) que se encontram [aqui](https://github.com/BM-a81824/Epidemiologia/tree/master/SIG-FinalProject/Figures/WW).



### Trabalho realizado por

Bárbara Martins, A81824



