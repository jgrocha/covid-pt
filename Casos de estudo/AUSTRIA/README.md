# COVID-19 AUSTRIA

 Author: Marcelo de Freitas Marreiros A82436
 
 Directory created to submit the Final Project made in scope of the "Systems of Geographical Information" class lectured by [Professor Jorge Rocha](https://github.com/jgrocha).


 ## Motivation
 From the challenge to use Geografical data and Covid-19 data this project was developed. This project mostly relies on the tools provided by QGIS, more specifically PyQGIS. Additionaly it involved some data manipulation using csv files and the pandas library data frames. Lastly matplot lib was extensivly used to make the plots presented bellow.

 ## Data
 All the notebooks in this directory go to the sources of data to get the most up to date information. However this results in a small time window after midnight (00:00 GMT+1) when the data hasn't been updated and the notebooks won't run properly. If this problem occurs simply use the [backup data provided](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/covid_data/covid-19-at-backup-31-05-2020.csv) or simply don't run the bit of code that gets the covid-19 data from the source.

### COVID-19 DATA
 - 🗂️ [COVID 19 DATA AUSTRIA](https://github.com/MarcelodeFreitas/Epidemiology/tree/master/Study%20Cases/AUSTRIA/covid_data)
 	- most of the csv files in this folder result form manipulations in the various notebooks
 	- [data source repository](https://github.com/covid19-eu-zh/covid19-eu-data) , [austria dataset used](https://github.com/covid19-eu-zh/covid19-eu-data/blob/master/dataset/covid-19-at.csv)

 ### GEOGRAPHICAL DATA
 - 🗂️ [MAP AUSTRIA](https://github.com/MarcelodeFreitas/Epidemiology/tree/master/Study%20Cases/AUSTRIA/map)
 	- [download link](https://data.biogeo.ucdavis.edu/data/diva/adm/AUT_adm.zip)

 ### IMAGES
 - 🗂️ [IMAGES](https://github.com/MarcelodeFreitas/Epidemiology/tree/master/Study%20Cases/AUSTRIA/images)
 	- all images result from the Jupyter Notebooks in this directory


## MAPS

### 🗂️ [Deaths (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_deaths.ipynb)

![Deaths map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_deaths.png)


### 🗂️ [Confirmed Cases (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_cases.ipynb)

![Confirmed cases map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_cases.png)


### 🗂️ [Recovered (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_recovered.ipynb)

![Recovered map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_recovered.png)



### 🗂️ [Tests (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_tests.ipynb)

![Tests map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_tests.png)



### 🗂️ [Hospitalized (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_hospitalized.ipynb)

![Hospitalized map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_hospitalized.png)


### 🗂️ [Intensive Care (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_map_intensive_care.ipynb)

![Intensive Care map](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/map_intensive_care.png)



## GRAPHS and STATISTICS

### 🗂️ [Graphs (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria-GRAPHS.ipynb)

#### BAR PLOTS

![deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/deaths.png)

![confirmed_cases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/confirmed_cases.png)

![recovered](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/recovered.png)

![tests](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/tests.png)

![hospitalized](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/hospitalized.png)

![intensive_care](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/intensive_care.png)

#### BAR PLOTS versus

![cases_vs_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/cases_vs_deaths.png)

![cases_vs_recovered](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/cases_vs_recovered.png)

![hospitalized_vs_intensive_care](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/hospitalized_vs_intensive_care.png)

#### BAR PLOTS versus 2.0

![hospitalized_vs_intensive_care_2](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/hospitalized_vs_intensive_care_2.png)

![cases_vs_deaths_2](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/cases_vs_deaths_2.png)

![cases_vs_recovered_2](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/cases_vs_recovered_2.png)

![tests_vs_deaths_2](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/tests_vs_deaths_2.png)

#### PIE PLOTS 

![pie_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_deaths.png)

![pie_cases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_cases.png)

![pie_recovered](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_recovered.png)

![pie_tests](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_tests.png)

![pie_hospitalized](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_hospitalized.png)

![pie_intensive_care](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/pie_intensive_care.png)




### 🗂️ [Statistics (more graphs) (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_statistics.ipynb)


In order to fit the labels instead of the datetime objects it is only displayed number of entries.

An example of the entries taken at 01-06-2020:

![date_time](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/date_entries.png)

#### LINE PLOTS

![time_cases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_cases.png)

![time_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_deaths.png)

![time_recovered](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_recovered.png)

![time_tests](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_tests.png)

There seems to be some missing hospitalization data in the beginning.

![time_hospitalized](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_hospitalized.png)

![time_intensive_care](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_intensive_care.png)

#### LINE PLOTS versus

![time_cases_recovered_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_cases_recovered_deaths.png)

![time_hospitalized_intensive_care_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_hospitalized_intensive_care_deaths.png)


#### LINE PLOTS evolution by state

Since the data entries are not uniform for every state, the entries are counted and the biiggest possible number is used. Example: [202, 203, 204, 206, 207, 208, 209, 209, 209] - -> 202 , in this cased the data for the graphs is restricted to [0:202].

There is also some abnormality in the cases confirmed by state.

![time_cases_state](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_cases_state.png)


![time_deaths_state](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_deaths_state.png)



### 🗂️ [Predictions (.ipynb)](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/COVID-19_Austria_predictions.ipynb)


![time_unique_deaths_cases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/time_unique_deaths_cases.png)

![prediction_numberofcases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/prediction_numberofcases.png)

![prediction_numberofdeaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/prediction_numberofdeaths.png)

#### Parametric Fitting

![parametric_cases](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/parametric_cases.png)

![parametric_deaths](https://github.com/MarcelodeFreitas/Epidemiology/blob/master/Study%20Cases/AUSTRIA/images/parametric_deaths.png)
