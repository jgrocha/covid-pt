# Mapping of COVID-19 (coronavirus) data, Statistical Analysis and Parametric Curve Fitting

This project is a collection of Jupyter notebooks:

🗂️ [Mapping of COVID-19 data (.ipynb)](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Maps.ipynb)

🗂️ [Statistical Analysis of COVID-19 data(.ipynb)](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Statistics.ipynb). 

🗂️ [Parametric Curve Fitting for Iceland(.ipynb)](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Forecasting.ipynb). 

Due to rendering issues we advise the use of [`nbviewer.jupyter.org`](https://nbviewer.jupyter.org/github/eduardavieira/epidemiologia/blob/master/COVID19-Project/Statistics.ipynb) to visualize all graphics or to consult the [Figures link](https://github.com/eduardavieira/epidemiologia/tree/master/COVID19-Project/Figures). 


## Dataset

The Dataset is part of the [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data/) repository on GitHub.

For a full variables description consult ([`owid-covid-data-codebook.md`](https://github.com/owid/covid-19-data/tree/master/public/data/owid-covid-data-codebook.md)).

## Motivation

One of the goals of this project was to understand how the economy, medical preparedness and population ageing influenced the number of cases of COVID-19 and consequent deaths.
Thus a dataset with the GDP per data of each country, extreme poverty levels, number of hospitals beds per 100K and share of population over 65 years old was used.

The Statistical Analysis allowed us to achieve this goal.

## Results


### Mapping

In the Figure below it is possible to consult the map that contains COVID-19 death cases across the world.

![death map](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/death_cases_map.png?raw=true)


### Statistical Analysis

In the Figure below it is possible to consult the Top 15 countries with the highest share of population 65 years and older.

![Top_65](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/top_15_aged_65.png?raw=true)

In Figure below a bubble chart containing the 60 countries with the highest share of population 65 years and older and the number of deaths per million of each country can be consulted.

The countries with most prevalent population ageing, such as Belgium, Spain, United Kingdom, Italy, France and Sweden, have also the highest values of death cases per million.

It is also worth noting that countries such as Portugal (second most population aged country) and Germany (fourth most population aged country) do not have such high values of death cases per million, mostly due to severe policies regarding quarentine.

![bubble_65](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/bubble_aged65_deaths_per_million.png?raw=true)

In Figure below a bubble chart containing the 50 countries with the highest share of the population living in extreme poverty and the number of deaths per million of each country can be consulted.

As we can see the poorest countries aren't the countries with the highest values of deaths per million.

![bubble_poverty](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/bubble_extreme_poverty_deaths_per_thousand.png?raw=true)

In Figure below a bubble chart containing the 70 countries with the highest Gross domestic product at purchasing power parity (constant 2011 international dollars) - GDP per capita and the number of tests per thousand of each country can be consulted.

It is possible to see that the countries with high GDP per capita do more tests per thousand and generally, low GDP per capita have do lower number of tests. With remarcable exceptions such as Bahrain. 

![bubble_gdp](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/bubble_gdp_tests_per_thousand.png?raw=true)

In the Figure below it is possible to consult the evolution of COVID-19 cases in China, it is clear that the evolution of the curve is logistic.

![cases_china](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/cases_China.png?raw=true)

In the Figure below it is possible to consult the evolution of COVID-19 death cases in Portugal.

![deaths_portugal](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/death_cases_portugal.png?raw=true)

### Parametric Curve Fitting of Iceland Cases

The objective of curve fitting is to find the optimal combination of parameters that minimize the error.

In the Figure below it is possible to consult the number of cases in Iceland (black dots) and the three models (logistic-blue, exponential-green and linear-red) attempting to fit the Iceland curve. It is clear that the best model is the logistic.

![curve_1](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/prediction_curve_1.png?raw=true)

The curve of new cases adjusts to a Gaussian function, see Figure below.

![new_cases](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/prediction_curve_2.png?raw=true)

The result of finding the optimal parameters (values of coefficients that minimize the fitting error) for the logistic model to forecast the number of cases can be consulted in the Figure below. 

![Prediction Iceland](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/prediction_parametric_fitting.png?raw=true)

The forecasting for the number of new cases is the result of finding the optimal parameters (values of coefficients that minimize the fitting error) for the Gaussian model, consult Figure below.

![Prediction Iceland](https://github.com/eduardavieira/epidemiologia/blob/master/COVID19-Project/Figures/prediction_parametric_fitting_new_cases.png?raw=true)