# Epidemiologia

A83280 - José Alexandre Ribeiro Ferreira


Para a realização deste trabalho foi utilizada a linguagem python, o QGis e o PostgreSQL.

# Mapas da Austrália

Os mapas criados são relativos à Austrália quer a nível local, regional e do país po inteiro.

A nível local:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Mapas/aus.png)

A nível das regiões e com graduação de tons de vermelho:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Mapas/aus_regions_vermelho.png)

# Estatísticas da Austrália

A nível local:

Foram criados gráficos de forma a expor os dados de forma mais facilmente percetível.

O primeiro é um gráfico de barras com as 10 localidades com mais casos confirmados de COVID-19. Também evidencia que Waverley é a localidade mais afetado conforme os dados disponíveis. A segunda é Sydney e é de destacar que ambas as localidades são próximas.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Bar10.png)

A próxima imagem possui as 22 localidades com mais casos. O número de casos neste gráfico encontra-se sob a forma de percentagem.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Pie22.png)

A nível das regiões:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Region_Bar.png)

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Region_Pie.png)

Estas duas imagens evidenciam que apenas três regiões possuem casos confirmados de COVID-19. Sendo elas New South Wales, Victoria e Western Australia.

A nível do país por um todo:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Country.png)

O gráfico evidencia que a quantidade de casos de COVID-19 na Austrália nem é possível visualizar em relação à população total do país.

Time Series - A nível das regiões:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Region_Evolution_Confirmed.png)
![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Region_Evolution_Recovered.png)
![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Region_Evolution_Deaths.png)

Estes três gráficos evidenciam que a região de New South Wales é a que apresenta o maior número de casos confirmados, de recuperados e de fatalidades. É de destacar que a região de Victoria foi a única que teve um maior número de recuperados no início.

Time Series - A nível do país por um todo:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Australia_Evolution.png)

A figura evidencia que a quantidade de casos novos e de recuperados está a estabilizar, embora continuem a aumentar. 
O número de fatalidades ao longo do tempo foi sempre muito próximo de 0 devido a ser um valor muito inferior aos outros dois.


![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Australia_Evolution_Confirmed.png)

Neste gráfico foram adicionadas as curvas relativas à média móvel(moving average) e o desvio padrão(rolling standard deviation) à curva da evolução do número de casos ao longo do tempo. 
Também foram criados gráficos para os recuperados e as fatalidades.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Australia_Evolution_Confirmed_Forecasting.png)

A imagem possui um gráfico ao qual foram adicionadas as curvas de forecasting de simples alisamento exponencial para alfa igual a 0,2, a 0,6 e ao valor que o modelo otimiza automaticamente. É de destacar que o alfa otimizado foi o que sempre se manteve mais próximo do valor real e o menor alfa teve as previsões mais afastadas desse valor.
Foram obtidas as previsões para os 10 dias seguintes, as quais evidenciam que o número de novos casos se está a estabilizar.
Também foram criados gráficos para os recuperados e as fatalidades.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Australia_Evolution_Confirmed_Forecasting_Model.png)

Nesta imagem encontra-se o gráfico em que se adicionaram as curvas de forecasting de tendência linear e de tendência aditiva de amortecimento de Holt's. Estas curvas também realizam a previsão dos 10 dias seguintes. Os valores obtidos foram bastante próximos e as previsões são de uma continuação do aumento do número de casos.
Também foram criados gráficos para os recuperados e as fatalidades.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Austr%C3%A1lia/Imagens/Estat%C3%ADsticas/Australian_Cases_Australia_New.png)

Este gráfico permite ver os novos casos confirmados, os recuperados e as fatalidades em cada dia. Ele evidencia que o pico de novos casos está ultrapassado, sendo que o número se começa a estabilizar.


# Mapas do Mundo

Os mapas criados são relativos ao número de casos confirmados por país e ao número de fatalidades em cada um.
Também é importante referir que os dados nesta imagem se encontram mais atualizados e por isso existir um maior número de casos comparado ao usado para fazer os mapas da Austrália.

A nível do número total de casos confirmados:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Mundo/Imagens/Mapas/world_vermelho_total.png)

A nível do número total de fatalidades:

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Mundo/Imagens/Mapas/world_preto_total.png)

# Estatísticas do Mundo


![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Mundo/Imagens/Estat%C3%ADsticas/World_Cases_Bar22.png)

O gráfico de barras verticais possui os países ordenados pelo número de casos confirmados, barra a vermelho. A barra a preto indica o número de fatalidades que cada um destes países apresnta. Também é de se destacar que a Austrália não se encontra entre os 22 países com mais casos, representados no gráfico.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Mundo/Imagens/Estat%C3%ADsticas/World_Cases_Pie10.png)

A imgem tem um gráfico circular em que estão presentes os 22 países com mais casos e os restantes estão na categoria Outras. Aqui é possível destacar a alta percentagem dos Estados Unidos da América. 

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/Mundo/Imagens/Estat%C3%ADsticas/World_Cases_Barh22.png)

Esta gráfico de barras horizontais tem o número de casos confirmados para cada um dos países.

# SQL

Possui dois exercícios simples dos quais se pretendeu importar dados da base de dados postgres e usá-los para fazer tabelas e gráficos.

# GitHub

Esta pasta possui um notebook com o qual se pretendeu importar um dataset diretamente de um link para o GitHub.

# QGis

Nesta pasta foi utilizado o QGis para criar um geopackage com um mapa de Portugal graduado em vermelho para destacar os concelhos e distritos com maior número de casos de COVID-19.

![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/QGis/Imagens/portugal_vermelho_concelhos.png)


![Image description](https://github.com/jose-alexandre98/Epidemiologia/blob/master/QGis/Imagens/portugal_vermelho_distritos.png)


# Webgrafia

O dataset Australian_Cases_by_LGA.csv encontra-se disponível em: https://covid19-esriau.hub.arcgis.com/datasets/australian-cases-by-lga/data?geometry=65.655%2C-40.480%2C-160.840%2C-13.453&showData=true

Os shapefiles da Austrália encontram-se no AUS_adm.zip, que está disponível em: https://data.biogeo.ucdavis.edu/data/diva/adm/AUS_adm.zip

Os shapefile do mapa mundo encontram-se em: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/

O dataset 20200512.csv está disponível no link: https://raw.githubusercontent.com/jgrocha/covid-pt/master/European%20Centre%20for%20Disease%20Prevention%20and%20Control/20200512.csv

Os datasets sobre o time_series foram importados pelos seguintes links:

https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv

https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv

https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv

