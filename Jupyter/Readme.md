# QGIS, Python e notebooks

A partir do momento em que é preciso tratar sistematicamente muitos dados geográficos e temporais ou repetir muitas vezes o mesmo tipo de processamento, precisamos de usar **programação**. Esta programação está orientada ao tratamento de dados geográficos, com uma componente temporal.

Os dados da distribuição do COVID-19 são naturalmente geográficos e com uma componente temporal. São dados adequados para começar a aprender **Programação de informação espaciotemporal**.

Vamos usar:
1. A linguagem Python e alguns ods seu mais conhecidos módulos, como `pandas` e `matplotlib`
1. O PyQGIS (explorar o QGIS a partir do Python)
1. O Jupyter (que nos permite simultaneamente programar e documentar)

## Instalação no Windows

Comece por instalar o QGIS, usando a versão com o instalador OSGeo4W. Ao instalar o QGIS, está também a instalar um ambiente Python.

### Instalação do Jupyter 

Em Windows, a solução passa por instalar e arrancar o Jupyter no **ambiente Python do QGIS**. Pode-se fazer isso alterando a sccript `python-qgis.bat` em `OSGeo4W64\bin\`, acrescentando no fim:
```
pip install notebook
jupyter notebook --notebook-dir <diretoria do trabalho>
```

### Partilhar um notebook

Os notebooks podem ser partilhados através dos repositórios do github. Caso o render não fique perfeito, pode-se usar o [nbviewer](https://nbviewer.jupyter.org/).

### Exemplos introdutórios

1.  Adicionar um layer e gerar uma imagem: [qgis.ipynb](qgis.ipynb)
1.  Abrir um projeto QGIS existente e gerar uma composição de impressão já preparada: [Explorar um projeto QGIS no Jupyter.ipynb](Explorar%20um%20projeto%20QGIS%20no%20Jupyter.ipynb)
1.  Ligar e tirar partido dos dados numa base de dados Postgresql: [SQL no Jupyter.ipynb](SQL%20no%20Jupyter.ipynb)

### Exercícios introdutórios

1.  Cruzar dados de uma tabela com um mapa, com os dados do ECDC: [ECDC.ipynb](ECDC.ipynb)
1.  Cruzar dados de uma tabela com um mapa, com os dados da JHU e mapas do Natural Earth: [JHUeNE.ipynb](JHUeNE.ipynb)

### Introdução aos modelos matemáticos

https://thedatafrog.com/en/articles/covid-19-analysis-uncertainties/

https://towardsdatascience.com/covid-19-infection-in-italy-mathematical-models-and-predictions-7784b4d7dd8d

https://medium.com/analytics-vidhya/how-to-predict-when-the-covid-19-pandemic-will-stop-in-your-country-with-python-d6fbb2425a9f

#### Exercício

1.  Curva logística para os dados de Portugal: [Curva logística.ipynb](Curva%20logística.ipynb)