# Base de dados Postgresql

## Restore

Este _restore_ cria a base de dados `covid` e recuperas as diversas tabelas geográficas e não-geográficas.

```
pg_restore --host=localhost --port=5433 --username=geobox -d postgres --create --verbose covid-20200424.backup
```

## Backup

O backup que é feito para passar para o repositório é:

```
pg_dump --verbose --host=localhost --port=5432 --username=covid --format=c --no-privileges --no-owner covid -f covid-20200424.backup
```

