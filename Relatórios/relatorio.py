#!/usr/bin/python3

# usage: ./relatorio2.py 2020-04-21 https://covid19.min-saude.pt/wp-content/uploads/2020/04/50_DGS_boletim_20200421.pdf 50_DGS_boletim_20200421.sql

import sys, argparse
import subprocess
import re
from concelhos import municipalities
import difflib
from datetime import datetime

def best_match(sqlfile, name, cases):
   canonical = difflib.get_close_matches(name.upper(), municipalities.keys(), n=1)
   dico = ''
   concelho = ''
   if len(canonical) == 1:
      dico = municipalities[canonical[0]]
      concelho = canonical[0]
      # print(name, canonical[0], dico, cases)
      print(canonical[0], end =" ")
   else:
      if name == "Lagoa (Faro)":
         dico = '0806'
         concelho = 'LAGOA'
         # print(name, 'LAGOA', '0806', cases)
      else:
         dico = '0000'
         concelho = name
         print("--ERROR------------------------------")
         print(name, canonical, cases)
         print("--ERROR------------------------------")
   sqlfile.write("-- {} \n".format( concelho ))
   altdate = datetime.fromisoformat(args.date)
   sqlfile.write("UPDATE public.confirmados_concelho SET \"{}\" = {} where dico = '{}';\n".format( altdate.strftime("%d/%m/%Y"), cases, dico ))

def fix_municipality_list(municipality):
   # municipalities with names broken
   idx = 0
   while idx < len(municipality):
      # print("{} > {}".format(idx, municipality[idx]))
      if re.match('^Penaguião', municipality[idx], re.IGNORECASE):
         municipality[idx-1] = " ".join([ municipality[idx-1], municipality[idx] ])
         municipality.pop(idx)
      if re.match('^Rodrigo', municipality[idx], re.IGNORECASE):
         municipality[idx-1] = " ".join([ municipality[idx-1], municipality[idx] ])
         municipality.pop(idx)
      if re.match('^Monsaraz', municipality[idx], re.IGNORECASE):
         municipality[idx-1] = " ".join([ municipality[idx-1], municipality[idx] ])
         municipality.pop(idx)
      m = re.search('^(\D+) (\d+)$', municipality[idx])
      if m:
         municipality[idx] = m.group(1)
         municipality.insert(idx+1, m.group(2))
         #print("..............{}..........{}..{}.....".format(municipality[idx], m.group(1), m.group(2)))
         idx += 1         
      idx += 1
   return municipality

def parse_municipality(municipality, sqlfile):
   municipality = fix_municipality_list(municipality)
   # print(municipality)
   idx = 0
   while idx < len(municipality):
      if not municipality[idx].isdigit():
         if (idx+1) < len(municipality) and not municipality[idx+1].isdigit():
            if (idx+2) < len(municipality) and not municipality[idx+2].isdigit():
               if not municipality[idx+3].isdigit():
                  # print(municipality[idx])
                  best_match(sqlfile, municipality[idx], municipality[idx+4])
                  best_match(sqlfile, municipality[idx+1], municipality[idx+5])
                  best_match(sqlfile, municipality[idx+2], municipality[idx+6])
                  best_match(sqlfile, municipality[idx+3], municipality[idx+7])
                  idx += 7
               else:
                  best_match(sqlfile, municipality[idx], municipality[idx+3])
                  best_match(sqlfile, municipality[idx+1], municipality[idx+4])
                  best_match(sqlfile, municipality[idx+2], municipality[idx+5])
                  idx += 5
            else:
               best_match(sqlfile, municipality[idx], municipality[idx+2])
               best_match(sqlfile, municipality[idx+1], municipality[idx+3])
               idx += 3
         else:
            best_match(sqlfile, municipality[idx], municipality[idx+1])
      idx += 1


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

# concelhos
# 1 coluna
pagina = 3
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 70 -y 420 -W 214 -H 1166 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
# print(dados)
dados.remove('CONCELHO')
dados.remove('NÚMERO')
dados.remove('DE CASOS')
parse_municipality(dados, sqlfile)

# 2 coluna
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 300 -y 420 -W 210 -H 1166 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
# print(dados)
dados.remove('CONCELHO')
dados.remove('NÚMERO')
dados.remove('DE CASOS')
parse_municipality(dados, sqlfile)

# 3 coluna
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 515 -y 420 -W 215 -H 1166 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
# print(dados)
dados.remove('CONCELHO')
dados.remove('NÚMERO')
dados.remove('DE CASOS')
parse_municipality(dados, sqlfile)

# 4 coluna
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 740 -y 420 -W 210 -H 1166 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
# print(dados)
dados.remove('CONCELHO')
dados.remove('NÚMERO')
dados.remove('DE CASOS')
parse_municipality(dados, sqlfile)

# 5 coluna
stdoutdata = subprocess.getoutput("pdftotext -f {} -l {} -r 150 -x 950 -y 420 -W 210 -H 1166 {} -".format(pagina, pagina, report))
dados = list(filter(None, stdoutdata.splitlines()))
# print(dados)
dados.remove('CONCELHO')
dados.remove('NÚMERO')
dados.remove('DE CASOS')
parse_municipality(dados, sqlfile)

print()

sqlfile.close()