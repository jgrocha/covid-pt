# ***COVID-19*** - Mapeamento de dados e Análise Estatística

Com vista a uma melhor compreensão do impacto global da COVID-19, foi desenvolvido um conjunto de notebooks onde se analisa as principais características disponibilizadas nos datasets utilizados, procedendo-se à criação de mapas e representações gráficas com bases nesses parâmentros. Foi ainda estudado com maior incidência este impacto no nosso país - Portugal - bem como na Espanha, de forma a permitir uma comparação com o país vizinho, e nos Estados Unidos, uma vez que é, até à data (30-05-2020), o país mais afetado pela COVID-19.

---

### Dados
Para a realização deste projeto, teve-se essencialmente em conta as seguintes fontes de dados:

| Fontes  |  Descrição  |
| ------------------- | ------------------- |
|  [GitHub - jgrocha](https://github.com/jgrocha/covid-pt) |  Dados relativos à situação epidemiológica de Portugal |
|  [GitHub - mdipietro09](https://github.com/mdipietro09/DataScience_ArtificialIntelligence_Utils/blob/master/time_series/example_parametric_fit.ipynb) - [Time Series Forecasting](https://medium.com/analytics-vidhya/how-to-predict-when-the-covid-19-pandemic-will-stop-in-your-country-with-python-d6fbb2425a9f) |  Auxílio na implementação de modelos de previsão |
| [data.world - COVID-19 in Spain](https://data.world/liz-friedman/covid-19-in-spain)  | Dados em formato csv referentes à situação epidemiológica em Espanha, descrevendo os casos a nível nacional |
| [CSSE - Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)  | Dados em formato csv referentes à situação epidemiológica mundial e dos Estados Unidos |
| [The New York Times - COVID-19_data](https://github.com/nytimes/covid-19-data)  | Dados em formato csv referentes aos Counties e Estados dos US  |

---

### Notebooks
No âmbito da exploração dos dados anteriores, relativos a casos de COVID-19, implementou-se um conjunto de notebooks:

- Mapeamento dos dados a nível mundial, a nível nacional, em Espanha e nos Estados Unidos da América
    - [Mapas](/COVID_19/mapas/Mapas.ipynb)

- Análise estatística a nível mundial - casos confirmados/ativos/recuperados, número de mortes e aplicação de modelos de previsão
    - [Situação Mundo](/COVID_19/dados_estatísticos/Situacao_Mundo.ipynb)

- Análise estatística a nível nacional - casos, influência do sexo/idade e sintomas desenvolvidos
    - [Situação PT](/COVID_19/dados_estatísticos/Situação_PT.ipynb)

- Análise estatística em Espanha - casos confirmados/recuperados/hospitalizados, casos nos cuidados intensivos, número de mortes e número de testes realizados
   - [Situação ESP](/COVID_19/dados_estatísticos/Situacao_SP.ipynb)

- Análise estatística nos Estados Unidos - casos confirmados/recuperados/ativos, casos hospitalizados, casos nos cuidados intensivos, casos utilizando ventilador, testes negativos/positivos e número de mortes
   - [Situação US](/COVID_19/dados_estatísticos/Situação_US.ipynb)

---

### Resultados
Foram obtidas figuras que descrevem os mapas relativos:

- ao número de casos confirmados no mundo:
![confirmados_mundo](/COVID_19/figuras/confirmados_mundo.png)

- ao número de casos confirmados em Portugal (por distrito):
![confirmados_portugal](/COVID_19/figuras/confirmados_distrito.png)

- ao número de casos confirmados em Espanha:
![confirmados_espanha](/COVID_19/figuras/confirmados_esp.png)

- ao número de casos confirmados nos Estados Unidos:
![confirmados_usa](/COVID_19/figuras/confirmados_usa.png)

Assim como figuras alusivas a dados estatíscos de casos de COVID-19:

- Países com maior número de casos confirmados:
![confirmados_mundo](/COVID_19/figuras/dados1_mundo.png)

- Número de casos confirmados por distrito em Portugal:
![confirmados_pt](/COVID_19/figuras/dados1_pt.png)

- à previsão do número de casos em Portugal, com a utilização de Modelos de Previsão:
![confirmados_portugal](/COVID_19/figuras/portugal_fit_model.png)

De forma a se proceder a esta previsão do números de casos, foi utilizado o [modelo de previsão](https://github.com/mdipietro09/DataScience_ArtificialIntelligence_Utils/blob/master/time_series/ts_utils.py) da autoria de [mdipietro09](https://github.com/mdipietro09).
Assim, com a utilização da script foi possível se definir os parâmetros a utilizar em cada função - linear, exponencial, logística, gaussiana - levando a que, consequentemente, se encontre o modelo que melhor se relacionava e ajusta ao número de casos confirmados em Portugal, permintido obter a seguinte previsão:
![previsao_portugal](/COVID_19/figuras/previsao_confirmados.png)

- aos principais sintomas sentidos por casos confirmados em Portugal:
![confirmados_portugal](/COVID_19/figuras/portugal_sintomas.png)

- Número de casos confirmados em Espanha:
![confirmados_sp](/COVID_19/figuras/dados1_esp.png)

- Counties com maior número de casos confirmados nos US:
![confirmados_us](/COVID_19/figuras/dados2_us.png)

- Número de casos confirmados vs Número de mortes:
![confirmados_mundo](/COVID_19/figuras/dados1_us.png)

---
