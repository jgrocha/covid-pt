#!/usr/bin/python3

# usage: ./relatorio2.py 2020-04-21 https://covid19.min-saude.pt/wp-content/uploads/2020/04/50_DGS_boletim_20200421.pdf 50_DGS_boletim_20200421.sql

import sys, argparse
import subprocess
import re
from concelhos import municipalities
import difflib
from datetime import datetime

def generate_sql(sqlfile, concelhos, casos):
   idx = 0
   while idx < len(concelhos):
      if concelhos[idx] == 'Lagoa (Faro)':
         dico = '0806'
      elif concelhos[idx] == 'Calheta (Madeira)':
         dico = '3101'
      else:
         dico = municipalities[concelhos[idx]]
      sqlfile.write("-- {} \n".format( concelhos[idx] ))
      altdate = datetime.fromisoformat(args.date)
      sqlfile.write("UPDATE public.confirmados_concelho SET \"{}\" = {} where dico = '{}';\n".format( altdate.strftime("%d/%m/%Y"), casos[idx], dico ))
      idx += 1

def fix_municipality_list(municipality):
   idx = 0
   while idx < len(municipality):
      canonical = difflib.get_close_matches(municipality[idx].upper(), municipalities.keys(), n=1)
      if canonical:
         score_alone = difflib.SequenceMatcher(None, municipality[idx].upper(), canonical[0]).ratio()
         print("{} → {} → {}".format(score_alone, municipality[idx].upper(), canonical[0]))
         if score_alone < 1.0 and idx < len(municipality)-1:
            score_with_next = difflib.SequenceMatcher(None, " ".join([municipality[idx].upper(), municipality[idx+1].upper()]), canonical[0]).ratio()
            print(" {} → {}".format(score_with_next, " ".join([municipality[idx].upper(), municipality[idx+1].upper()]) ))
            if score_alone < score_with_next:
               canonical = difflib.get_close_matches(" ".join([municipality[idx].upper(), municipality[idx+1].upper()]), municipalities.keys(), n=1)
               municipality[idx] = canonical[0]
               municipality.pop(idx+1)
            else:
               municipality[idx] = canonical[0]
         else:
            municipality[idx] = canonical[0]
      else:
         print("{} → {} → {}".format(0.0, municipality[idx].upper(), '--SEM MATCH--'))
      idx += 1
   return municipality


parser = argparse.ArgumentParser(description='Process DGS report')
parser.add_argument('date')
parser.add_argument('url')
parser.add_argument('sql')

args = parser.parse_args()
print(args.date)
print(args.url)
url = args.url
print(args.sql)
report = url[url.rfind("/")+1:]
print(report)

sqlfile = open(args.sql,"w+")
sqlfile.write("INSERT INTO public.situacao_epidemiologica (url,data_relatorio) VALUES ('{}', '{}');\n".format(args.url, args.date))

# 1a página
pagina = 1
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 456 -y 873 -W 150 -H 723 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
if len(valores) != 7:
   print("Problema na página {}".format(pagina))
else:
   sqlfile.write("UPDATE public.situacao_epidemiologica SET suspeitos = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET nao_confirmados = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET aguarda_resultados = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET recuperados = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos = {} where data_relatorio = '{}';\n".format(valores[5], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET em_vigilancia = {} where data_relatorio = '{}';\n".format(valores[6], args.date))

# 2a página
pagina = 2
# casos masculino
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 846 -y 1170 -W 130 -H 350 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
if len(valores) != 10 and sum(valores[0:9]) != valores[-1]:
   print("Problema na página {}".format(pagina))
else:
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_0_9 = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_10_19 = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_20_29 = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_30_39 = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_40_49 = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_50_59 = {} where data_relatorio = '{}';\n".format(valores[5], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_60_69 = {} where data_relatorio = '{}';\n".format(valores[6], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_70_79 = {} where data_relatorio = '{}';\n".format(valores[7], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_masculino_80_sup = {} where data_relatorio = '{}';\n".format(valores[8], args.date))

# casos feminino
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 1000 -y 1170 -W 130 -H 350 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
if len(valores) != 10 and sum(valores[0:9]) != valores[-1]:
   print("Problema na página {}".format(pagina))
else:
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_0_9 = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_10_19 = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_20_29 = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_30_39 = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_40_49 = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_50_59 = {} where data_relatorio = '{}';\n".format(valores[5], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_60_69 = {} where data_relatorio = '{}';\n".format(valores[6], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_70_79 = {} where data_relatorio = '{}';\n".format(valores[7], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET confirmados_feminino_80_sup = {} where data_relatorio = '{}';\n".format(valores[8], args.date))

# casos importados
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 20 -y 850 -W 585 -H 785 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
# print(dados);
nums = []
for i in dados: 
   nums.extend( re.findall(r'\d+', i) )
valores = [int(i) for i in nums] 
print("CASOS IMPORTADOS: {}".format(sum(valores)));
sqlfile.write("UPDATE public.situacao_epidemiologica SET importados = {} where data_relatorio = '{}';\n".format(sum(valores), args.date))

# 4a página
pagina = 4
# caracterização clínica
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 124 -y 457 -W 956 -H 61 {} -".format(pagina, pagina, report))
print( stdoutdata.splitlines() )
dados = list(filter(str.isdigit, stdoutdata.splitlines()))
valores = [int(i) for i in dados] 
print(valores);
sqlfile.write("UPDATE public.situacao_epidemiologica SET internados = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET internados_uci = {} where data_relatorio = '{}';\n".format(valores[1], args.date))

# ,,,,,

stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 192 -y 708 -W 859 -H 40 {} -".format(pagina, pagina, report))
print( stdoutdata.splitlines() )
dados = list(filter(str.isdigit, [x.strip('%') for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_febre = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_tosse = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_respiratoria = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_cefaleia = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_dores = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
sqlfile.write("UPDATE public.situacao_epidemiologica SET sintoma_fraqueza = {} where data_relatorio = '{}';\n".format(valores[5], args.date))

# óbitos
# casos masculino
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 551 -y 1060 -W 140 -H 345 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
if len(valores) != 10 and sum(valores[0:9]) != valores[-1]:
   print("Problema na página {}".format(pagina))
else:
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_0_9 = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_10_19 = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_20_29 = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_30_39 = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_40_49 = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_50_59 = {} where data_relatorio = '{}';\n".format(valores[5], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_60_69 = {} where data_relatorio = '{}';\n".format(valores[6], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_70_79 = {} where data_relatorio = '{}';\n".format(valores[7], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_masculino_80_sup = {} where data_relatorio = '{}';\n".format(valores[8], args.date))

# óbitos
# casos feminino
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 712 -y 1060 -W 140 -H 345 {} -".format(pagina, pagina, report))
dados = list(filter(None, [x.strip() for x in stdoutdata.splitlines()]))
valores = [int(i) for i in dados] 
print(valores);
if len(valores) != 10 and sum(valores[0:9]) != valores[-1]:
   print("Problema na página {}".format(pagina))
else:
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_0_9 = {} where data_relatorio = '{}';\n".format(valores[0], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_10_19 = {} where data_relatorio = '{}';\n".format(valores[1], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_20_29 = {} where data_relatorio = '{}';\n".format(valores[2], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_30_39 = {} where data_relatorio = '{}';\n".format(valores[3], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_40_49 = {} where data_relatorio = '{}';\n".format(valores[4], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_50_59 = {} where data_relatorio = '{}';\n".format(valores[5], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_60_69 = {} where data_relatorio = '{}';\n".format(valores[6], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_70_79 = {} where data_relatorio = '{}';\n".format(valores[7], args.date))
   sqlfile.write("UPDATE public.situacao_epidemiologica SET obitos_feminino_80_sup = {} where data_relatorio = '{}';\n".format(valores[8], args.date))

# # concelhos
print()
pagina = 3

#coluna 1
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 70 -y 453 -W 148 -H 1135 {} -".format(pagina, pagina, report))
stdoutcasos = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 219 -y 453 -W 57 -H 1135 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
casos = list(filter(None, stdoutcasos.splitlines()))
# print(dados)
dados = fix_municipality_list(dados)
print(casos)
print("Concelhos vs Casos: {} {}".format(len(dados), len(casos)))
generate_sql(sqlfile, dados, casos)

#coluna 2
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 300 -y 453 -W 144 -H 1135 {} -".format(pagina, pagina, report))
stdoutcasos = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 444 -y 453 -W 53 -H 1135 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
casos = list(filter(None, stdoutcasos.splitlines()))
# print(dados)
dados = fix_municipality_list(dados)
print(casos)
print("Concelhos vs Casos: {} {}".format(len(dados), len(casos)))
generate_sql(sqlfile, dados, casos)

#coluna 3
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 520 -y 453 -W 148 -H 1135 {} -".format(pagina, pagina, report))
stdoutcasos = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 668 -y 453 -W 53 -H 1135 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
casos = list(filter(None, stdoutcasos.splitlines()))
# print(dados)
dados = fix_municipality_list(dados)
print(casos)
print("Concelhos vs Casos: {} {}".format(len(dados), len(casos)))
generate_sql(sqlfile, dados, casos)

#coluna 4
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 740 -y 453 -W 134 -H 1135 {} -".format(pagina, pagina, report))
stdoutcasos = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 879 -y 453 -W 65 -H 1135 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
casos = list(filter(None, stdoutcasos.splitlines()))
# print(dados)
dados = fix_municipality_list(dados)
print(casos)
print("Concelhos vs Casos: {} {}".format(len(dados), len(casos)))
generate_sql(sqlfile, dados, casos)

#coluna 5
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 952 -y 453 -W 146 -H 1135 {} -".format(pagina, pagina, report))
stdoutcasos = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 1102 -y 453 -W 53 -H 1135 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
casos = list(filter(None, stdoutcasos.splitlines()))
# print(dados)
dados = fix_municipality_list(dados)
print(casos)
print("Concelhos vs Casos: {} {}".format(len(dados), len(casos)))
generate_sql(sqlfile, dados, casos)


sqlfile.close()