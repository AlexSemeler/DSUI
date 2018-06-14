# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018

@author: Alexandre Ribas Semeler
@author: Adislon Luiz Pinto
@author: Arthur L. Oliveira
"""
import codecs
import requests
from bs4 import BeautifulSoup
import lxml.objectify as obj
import lxml.etree as etree

print 'Início da coleta dos Links e Nomes das Coleções nos Repositórios.'

# função que seleciona as tags OAI-2.0 no XML de cada repositório 

def get_sets_list(some_url):
    triples_list = []
    html = requests.get(some_url).content
    soup = BeautifulSoup(html, "lxml")
    sets = soup.find_all('set')
    request_url = soup.find('request')
    try:
        pure_request_url = obj.fromstring('%s' % request_url)
    except etree.XMLSyntaxError:
        print 'XML syntax error on string: %s' % request_url
        return ''
    for item in sets:
        pair = obj.fromstring('%s' % item)
        triples_list.append([pure_request_url, pair.setspec, pair.setname])
    return triples_list

source = codecs.open('../dados/csv/IbictExtract.csv', 'r', 'utf-8-sig')
line_list = source.readlines()
source.close()
# escreve o conteudo do XML em um csvs contendo as coleções de cada repositório requisitado
with codecs.open('../dados/csv/teste-todas.csv', 'w', 'utf-8-sig') as output_csv:
    output_csv.write('request\tSetSpec\tSetName\n')
    for j in range(1, len(line_list)):
        try:
            url = line_list[j].split('\t')[0]
            print 'Extracting from: %s' % url
            set_list = get_sets_list(url)
            if set_list:
                for a_set in set_list:
                    output_csv.write('%s\t%s\t%s\n' % (a_set[0], a_set[1], a_set[2]))
        except requests.exceptions.ConnectionError:
            print 'Connection error with %s\nConnection aborted.' % url
        except requests.exceptions.MissingSchema:
            print 'Missing schema on %s\nConnection aborted.' % url
        except requests.exceptions.InvalidSchema:
            print 'No connection adapters found for %s.\n Check url for errors.' % url
        except requests.exceptions.ReadTimeout:
            print 'No connection adapters found for %s.\n Check url for errors.' % url    
output_csv.close()

print 'Extração Realizada com Sucesso.'
