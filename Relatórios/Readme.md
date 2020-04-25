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
cd Relatórios/
wget https://covid19.min-saude.pt/wp-content/uploads/2020/04/50_DGS_boletim_20200421.pdf
./relatorio.py 2020-04-21 https://covid19.min-saude.pt/wp-content/uploads/2020/04/50_DGS_boletim_20200421.pdf 50_DGS_boletim_20200421.sql
```
Inserir na base de dados:

```bash
psql service=covid -f 50_DGS_boletim_20200421.sql
psql service=covid -c 'update public.confirmados_concelho set mais_recente = "21/04/2020"'
```

Exportar para CSV:

```bash
psql service=covid -c "COPY situacao_epidemiologica TO STDOUT DELIMITER ',' CSV HEADER QUOTE '\"' FORCE QUOTE * " > ../situacao_epidemiologica.csv
psql service=covid -c "COPY confirmados_concelho TO STDOUT DELIMITER ',' CSV HEADER QUOTE '\"' FORCE QUOTE * " > ../confirmados_concelho.csv
```

Gerar o geopackage e os mapas em PNG, a partir do projeto QGIS:

```bash
cd ../geopackages
python3 2geopackage.py 2020-04-21
```

Atualizar o link para o último geopackage:

```bash
cd ..
./make-latest.sh
```
