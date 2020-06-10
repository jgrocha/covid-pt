# Mapping of COVID-19 data in USA, Statistical Analysis and Parametric Curve Fitting

Throughout this project, some notebooks were developed in order to study, through different parameters, the epidemiological situation of the coronavirus in the United States, one of the most affected countries by the virus.

## Dataset

The dataset used is part of a project called "COVID19 Tracking"(https://github.com/COVID19Tracking). This project provides the most complete data available about COVID-19 in the US.


To facilitate data access and analysis, these datasets have been changed. The datasets used are in [Dataset](https://github.com/claudiarmabreu/Epidemologia/tree/master/Projeto%20Covid-19/Dataset).


## Notebooks

In this project, the Jupyter notebooks developed were the following:

🗂️ [Mapping Covid-19 number of cases, deaths and recovered in USA (.ipynb)](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Notebooks/COVID19-US-Maps.ipynb)

🗂️ [Statistics and Parametric Curve Fitting of Covid-19 in USA (.ipynb)](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Notebooks/COVID19-US-Stats.ipynb)



## Mapping


### Number of cases in USA

This map shows the distribution of the number of cases on each state of the USA, in order to see the most affected states.


![case map](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/number_cases.png)


### Number of deaths in USA

This map shows the distribution of the number of deaths on each state of the USA, so we can see which states are unable to respond to the problem very well.


![death map](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/number_deaths_2.png)

### Number of recovered cases in USA

This map shows the distribution of the number of recovered cases on each state of the USA.


![recovered map](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/number_recovered.png)


## Statistical analysis

This [notebook](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Notebooks/COVID19-US-Stats.ipynb) presents several statistical analysis regarding Covid19 in USA. 

In this notebook, it is possible to find many top 5 and bottom 5 plots of number of cases, number of deaths, number of recovered and many others.

The TOP 5 Cases are presented on this figure.

![figure](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/Top5_cases.png)

The Bottom 5 Cases are presented on this figure.

![figure](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/Bottom5_cases.png)

### NY vs NJ

This next plot presents a comparison between the two most affected states, NY and NJ. It is clear that NY is the most affected state by far.

![nynj](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/NY_NJ.png)



### Currently ventilated Cases

This pie chart shows the percentage of cases currently ventilated on each state: 

![Currently ventilated Cases](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/Ventilated.png).


### Evolution of number of cases in NY

This [plot](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/cases_NY.png) shows the evolution of the number of positive cases in the state of New York, the most affected state, over the days, since the beginnig of this pandemic.

![plot](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/cases_NY.png)

### Evolution of number of recovered in NY

This [plot](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/Recovered_NY.png) shows the evolution of the number of recovered cases in NY.

![plot](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/Recovered_NY.png)

## Parametric Curve Fitting

In order to predict the increase on the number of cases on the following days, it was used a forecasting model. 
Through a curve adjustment, it was possible to find the model that best fitted the evolution of number of cases. The options studied were the logistic model, exponential model and linear model.
The black dots represent the number of cases so far and the three models are represent by the colored lines.

![curve](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/PCF.png) 

By observing the figure below, it is possible to verify that the logistic model is the most adequate

Accordingly, it was also possible to find the ideal parameters for the model under study and the result prediction is found in the figure below.

![prediction](https://github.com/claudiarmabreu/Epidemologia/blob/master/Projeto%20Covid-19/Images/PCF2.png)


## Work made by

Ana Cláudia Abreu A80276 

Biomedical Engineering student in the Master of Medical Informatics
University of Minho


## Date

27/05/2020