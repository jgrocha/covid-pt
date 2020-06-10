# Study of Covid-19 in Italy

Throughout this project, some notebooks were developed in order to study, through different parameters, the epidemiological situation of the coronavirus in Italy, the European country most affected by the virus.

## Dataset

The dataset used is part of a study carried out by [Imperial College London](https://github.com/ImperialCollegeLondon/covid19model/blob/master/Italy/data/dpc-covid19-ita-regioni.csv).

Throughout the development of the work, this dataset has undergone some changes that can be consulted in the folder [Dataset](https://github.com/kika-nogueira97/Epidemologia/tree/master/Projeto_Italy/Dataset).

## Notebooks

In this project, different Jupyter notebooks were developed:

🗂️ [Mapping covid-19 number of cases in Italy (.ipynb)](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_map_number_cases.ipynb)

🗂️ [Mapping covid-19 number of deaths in Italy (.ipynb)](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_map_deaths.ipynb)

🗂️ [Statistical analysis of covid-19 data in different regions (.ipynb)](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_statistic.ipynb)

🗂️ [Forecasting models (.ipynb)](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_prevision.ipynb)

🗂️ [Covid19 Animation - Number of cases per region (.ipynb)](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_animation.ipynb)

## Mapping


### Number of cases in Italy

On this map it is possible to see the distribution of the number of cases across the different regions of Italy.
If you want to visualize the distribution of the number of deaths in the different Italian regions, just consult this [image](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/Geographic_distribution_Number_deaths.png)

![case map](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/Geographic_distribution_Number_cases.png)


## Statistical analysis

Throughout this area of ​​study, numerous graphics have been made that can be consulted in this [nootbook](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_statistic.ipynb)

Through these examples, it is possible to compare the most affected regions with each other, through numerous criteria. 

### Piemonte vs Emilia-Romagna

With the equivalence of values ​​in numerous criteria, between Piemonte and Emilia-Romagna, there was a need to study the different areas and understand where these two regions stood out along the covid19.

![piemonte](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/comparation_piemonte_emilia.png)


### Lombardia vs Piemonte

As Lombardia and Piemonte were in the first and second place in the [Top 5 of regions with the highest number of cases](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/Top5_more_cases.png), we sought to understand the differences between these two regions, relative to the place of recovery/hospitalization.

![lombardia](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/comparation_lombardia_piemonte.png)

## Forecasting models

When using a forecasting model, it is possible, through a curve adjustment, to find the ideal combination of parameters, capable of minimizing errors.
Throughout the development of this Jupyter notebook, numerous [forecasting models](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Notebooks/Italy_prevision.ipynb) have been developed.
In the figure below it is possible to see the number of deaths in Molise (black dots) and the three models (blue - logistic, light blue - exponential and dark blue-linear) that try to fit the Molise curve. With the observation of the model it is possible to verify that the exponential model is the most adequate.

![curve](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/Prevision_molise_numberofdeaths.png) 

Accordingly, it was also possible to find the ideal parameters for the four models.

![prediction](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Imagens/prediction_molise.png)

## Gif Animation

To finish the work, a gif was developed capable of demonstrating the daily growth in the number of cases of covid 19, in the top 10 of regions most affected by italy.

![gif](https://github.com/kika-nogueira97/Epidemologia/blob/master/Projeto_Italy/Gif/Number%20of%20cases%20per%20region.gif)

## Work made by

Francisca Nogueira A81590 (Biomedical Engineering student in the Master of Medical Informatics, at the University of Minho)


## Date

24/05/2020