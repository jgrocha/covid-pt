# Projeto QGIS

O projeto QGIS apresentado tem camadas que vêem de uma base de dados Postgresql. O conteúdo da base de dados pode ser recriado a partir do backup que está na pasta [basededados](../basededados/).

## Ligação à base de dados

A ligação à base de dados é feita através de um [serviço](https://www.postgresql.org/docs/current/libpq-pgservice.html) `libpq` do Postgresql.

Terá que criar na sua pasta pessoal um arquivo `.pg_service.conf` (em Linux) com:

```
[covid]
host=localhost
dbname=covid
user=covid
password=covid
```

O nome do serviço `covid` é depois usado na ligação do QGIS à base de dados:

![](ligacao%20com%20libpq%20service.png)

### Em Windows

Se usar Windows, tem que definir uma variável de ambiente do utilizador designada `PGSYSCONFDIR` com o valor `%userprofile%` (que representa a sua pasta pessoal).

Na sua pasta pessoal, crie um arquivo `pg_service.conf` com o conteúdo:

```
[covid]
host=localhost
dbname=covid
user=covid
password=covid
```
