# Importação dos relatórios da DGS

## Script de importação

A script [relatorio.py](relatorio.py) faz a conversão do documento PDF da DGS para um script sql. Depois é preciso executar o código SQL para injetar os dados na base de dados.

```
usage: relatorio.py date url sql
```

A script sql atualiza duas tabelas:
1. `situacao_epidemiologica`
1. `confirmados_concelho`

O dicionário (na terminologia do Python) [concelhos.py](concelhos.py) é usado para encontrar o nome oficial do concelho mais parecido com o que aparece nos relatórios da DGS.

## Exemplo de execução

Gerar o sql:

```bash
hoje=$(date '+%Y%m%d')
ho_je=$(date '+%Y-%m-%d')
ho7je=$(date '+%d/%m/%Y')
cd Relatórios/
wget https://covid19.min-saude.pt/wp-content/uploads/2020/05/60_DGS_boletim_20200501.pdf
./relatorio.py $ho_je https://covid19.min-saude.pt/wp-content/uploads/2020/05/60_DGS_boletim_20200501.pdf 60_DGS_boletim_20200501.sql
```
Inserir na base de dados:

```bash
psql service=covid -f 60_DGS_boletim_20200501.sql
psql service=covid -c 'update public.confirmados_concelho set mais_recente = "'"$ho7je"'"'
```

Exportar para CSV:

```bash
psql service=covid -c "COPY (select * from situacao_epidemiologica order by data_relatorio) TO STDOUT DELIMITER ',' CSV HEADER QUOTE '\"' FORCE QUOTE * " -o ../situacao_epidemiologica.csv
psql service=covid -c "COPY (select * from public.confirmados_concelho order by dico) TO STDOUT DELIMITER ',' CSV HEADER QUOTE '\"' FORCE QUOTE * " -o ../confirmados_concelho.csv
```

Gerar o geopackage e os mapas em PNG, a partir do projeto QGIS:

```bash
cd ../geopackages
python3 2geopackage.py $ho_je
```

Atualizar o link para o último geopackage:

```bash
cd ..
./make-latest.sh
```

Dump da base de dados:

```bash
cd basededados
pg_dump --verbose --host=localhost --port=5432 --username=covid --format=c --no-privileges covid -f covid-$hoje.backup
```

Outros dados:

```bash
cd "../European Centre for Disease Prevention and Control"
wget https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/ -O $hoje.csv
```