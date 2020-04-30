Dados do European Centre for Disease Prevention and Control

Os dados atualizados diariamente sobre a distribuição geográfica dos casos de COVID-19 no mundo são descarregados a partir do link:

https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases

```bash
cd "../European Centre for Disease Prevention and Control"
hoje=$(date '+%Y%m%d')
wget https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/ -O $hoje.csv
```