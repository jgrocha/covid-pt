#!/usr/bin/python3

#
# Saca dados da mortalidade geral a partir de:
# https://evm.min-saude.pt/
#

import urllib.request
import re
import json
import csv

url = 'https://evm.min-saude.pt/table?t=geral&s=0'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8')

text = re.sub('^[^{]+', '', text, re.MULTILINE)
text = re.sub('</script>\n</div>$', '', text, re.MULTILINE)

dados = json.loads(text)

print(dados.keys())

# list
mortalidade = dados['x']['data']
# com 13 linhas: Data (mm-dd) 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020
print(len(mortalidade))
# print dias do ano
print(mortalidade[0])
# print valores para 2020
print(mortalidade[-1])