# Epidemiologia - Austrália

A83280 - José Alexandre Ribeiro Ferreira

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
