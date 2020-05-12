# Base de dados Postgresql

## Restore

Este _restore_ cria a base de dados `covid`, instala a extensão `postgis` e recupera as diversas tabelas geográficas e não-geográficas. Tem que ser invocada com um `role` que permita criar base de dados e instalar a extensão `postgis`.

```
pg_restore --host=localhost --port=5433 --username=geobox -d postgres --create --no-owner --verbose covid-20200424.backup
```

## Backup

O backup que é feito para passar para o repositório é:

```
pg_dump --verbose --host=localhost --port=5432 --username=covid --format=c --no-privileges covid -f covid-20200424.backup
```

# Comparação de dados entre diferentes base de dados Postgresql

Se necessário confrontar estes dados com dados outra base de dados Postgresql, pode-se usar uma **tabela remota**, de modo a se poder fazer queries entre duas tabelas, como estando na mesma base de dados.

Na base de dados `covid`:

```sql
CREATE EXTENSION postgres_fdw;

CREATE SERVER servidor_remoto
        FOREIGN DATA WRAPPER postgres_fdw
        OPTIONS (host 'localhost', port '5433', dbname 'covid');

CREATE USER MAPPING FOR CURRENT_USER
        SERVER servidor_remoto
        OPTIONS (user 'geobox', password 'geobox');

-- vamos por as tabelas da base de dados remota, num esquema local remota
CREATE SCHEMA remota;

-- se quisermos todas as tabelas remotas do esquema public
IMPORT FOREIGN SCHEMA public
  FROM SERVER servidor_remoto
  INTO remota;

-- se quisermos uma lista mais limitada de tabelas
IMPORT FOREIGN SCHEMA public LIMIT to (confirmados_concelho, situacao_epidemiologica)
  FROM SERVER servidor_remoto
  INTO remota;
```

## Queries

Podem-se então fazer queries usando tabelas no esquema `public` da nossa base de dados `covid` e tabelas do esquema `remota`.

```sql
select * from public.situacao_epidemiologica where data_relatorio  = '2020-04-04'
union all
select * from remota.situacao_epidemiologica where data_relatorio  = '2020-04-04';

select concelho, "04/04/2020", "04/05/2020" from public.confirmados_concelho cc  order by "04/04/2020" desc NULLS LAST;

select concelho, "04/04/2020", "04/05/2020" from remota.confirmados_concelho  order by "04/04/2020" desc NULLS last;
```

## Correção (em 2020-05-12)

O update do dia "04/05/2020" foi lançado no dia "04/04/2020". Ou seja, os dados de "04/04/2020" ficaram estragados.

Para corrigir, restaurou-se uma versão mais antiga da base de dados, anterior a "04/05/2020".

```sql
update public.confirmados_concelho b
set "04/04/2020" = a."04/04/2020"
from remota.confirmados_concelho a
WHERE a.concelho = b.concelho;

UPDATE public.situacao_epidemiologica b
SET   (url,data_relatorio,suspeitos,confirmados,nao_confirmados,aguarda_resultados,recuperados,obitos,em_vigilancia,confirmados_masculino_0_9,confirmados_masculino_10_19,confirmados_masculino_20_29,confirmados_masculino_30_39,confirmados_masculino_40_49,confirmados_masculino_50_59,confirmados_masculino_60_69,confirmados_masculino_70_79,confirmados_masculino_80_sup,confirmados_feminino_0_9,confirmados_feminino_10_19,confirmados_feminino_20_29,confirmados_feminino_30_39,confirmados_feminino_40_49,confirmados_feminino_50_59,confirmados_feminino_60_69,confirmados_feminino_70_79,confirmados_feminino_80_sup,importados,internados,internados_uci,sintoma_febre,sintoma_tosse,sintoma_respiratoria,sintoma_cefaleia,sintoma_dores,sintoma_fraqueza,obitos_masculino_0_9,obitos_masculino_10_19,obitos_masculino_20_29,obitos_masculino_30_39,obitos_masculino_40_49,obitos_masculino_50_59,obitos_masculino_60_69,obitos_masculino_70_79,obitos_masculino_80_sup,obitos_feminino_0_9,obitos_feminino_10_19,obitos_feminino_20_29,obitos_feminino_30_39,obitos_feminino_40_49,obitos_feminino_50_59,obitos_feminino_60_69,obitos_feminino_70_79,obitos_feminino_80_sup)
    = (a.url,a.data_relatorio,a.suspeitos,a.confirmados,a.nao_confirmados,a.aguarda_resultados,a.recuperados,a.obitos,a.em_vigilancia,a.confirmados_masculino_0_9,a.confirmados_masculino_10_19,a.confirmados_masculino_20_29,a.confirmados_masculino_30_39,a.confirmados_masculino_40_49,a.confirmados_masculino_50_59,a.confirmados_masculino_60_69,a.confirmados_masculino_70_79,a.confirmados_masculino_80_sup,a.confirmados_feminino_0_9,a.confirmados_feminino_10_19,a.confirmados_feminino_20_29,a.confirmados_feminino_30_39,a.confirmados_feminino_40_49,a.confirmados_feminino_50_59,a.confirmados_feminino_60_69,a.confirmados_feminino_70_79,a.confirmados_feminino_80_sup,a.importados,a.internados,a.internados_uci,a.sintoma_febre,a.sintoma_tosse,a.sintoma_respiratoria,a.sintoma_cefaleia,a.sintoma_dores,a.sintoma_fraqueza,a.obitos_masculino_0_9,a.obitos_masculino_10_19,a.obitos_masculino_20_29,a.obitos_masculino_30_39,a.obitos_masculino_40_49,a.obitos_masculino_50_59,a.obitos_masculino_60_69,a.obitos_masculino_70_79,a.obitos_masculino_80_sup,a.obitos_feminino_0_9,a.obitos_feminino_10_19,a.obitos_feminino_20_29,a.obitos_feminino_30_39,a.obitos_feminino_40_49,a.obitos_feminino_50_59,a.obitos_feminino_60_69,a.obitos_feminino_70_79,a.obitos_feminino_80_sup)
FROM   remota.situacao_epidemiologica a
WHERE  b.id = 33
AND    a.id = b.id;
```