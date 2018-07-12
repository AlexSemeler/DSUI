# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018

@author: Arthur L. Oliveira
"""

import codecs
import requests
from bs4 import BeautifulSoup
from collections import Counter
import lxml.objectify as obj
import lxml.etree as etree


def get_sets_list(some_url):        # function que recebe url e devolve lista de triplas (url, setspec, setname)
    triples_list = []               # inicializa lista de triplas
    html = requests.get(some_url, timeout=10).content   # function de acesso ao html, timeout em segundos
    soup = BeautifulSoup(html, "lxml")                  # parsing do html
    sets = soup.find_all('set')                         # sets = lista de todas as ocorrencias de 'set'
    request_url = soup.find('request')                  # request_url = proxima ocorrencia de 'request'
    if 'localhost' in str(request_url) or '127.0.0.1' in str(request_url):  # previne erros de localhost na url
        request_url = some_url.split('?')[0]
    try:
        pure_request_url = obj.fromstring('%s' % request_url)   # gera arvore de dados a partir de html para parsing
    except etree.XMLSyntaxError:                                # tratamento de exception
        print 'XML syntax error on string: "%s" was the request url' % request_url
        return ''                                               # retorna string vazia neste caso
    for item in sets:                                           # percorre 'sets' para preencher 'triples'
        pair = obj.fromstring('%s' % item)
        triples_list.append([pure_request_url, pair.setspec, pair.setname])
    return triples_list


try:
    source = codecs.open('CollectionPeriodicosList.csv', 'r', 'utf-8-sig')      # abre csv para leitura
except IOError:
    print 'Erro ao abrir IbictExtract.csv'
else:
    line_list = source.readlines()                                  # bufferiza csv
    source.close()                                                  # fecha csv
    setNameList = Counter()

    with open('xml_error_log.txt', 'w') as errors:  # txt para escrever log de erros
        csv_folder = '../Data Science/output_csvs/'
        print 'Begin of extraction:', len(line_list)-1, 'URLs to extract'
        for j in range(1, len(line_list)):                                  # percorre linhas do csv bufferizado
            try:
                url = line_list[j].split('\t')[0]           # extrai url da linha de csv
                # abre csv de output para escrita:
                print j, ': Extracting from: %s' % url
                set_list = get_sets_list(url)               # set_list <- lista de triplas (url, setspec, setname)
                if set_list:                                # trata lista caso ela exista
                    for a_set in set_list:                  # trata cada tripla para escrita no csv de output
                        csv_name = '%s' % a_set[2]
                        chars_to_remove = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']
                        for char in chars_to_remove:
                            csv_name = csv_name.replace(char, '-')
                        setNameList[a_set[2]] += 1
                        if setNameList[a_set[2]] > 1:
                            output_csv = codecs.open(csv_folder + csv_name, 'a', 'utf-8-sig')
                            output_csv.write('%s\t%s\n' % (a_set[0], a_set[1]))
                            output_csv.close()
                        else:
                            output_csv = codecs.open(csv_folder + csv_name, 'w', 'utf-8-sig')
                            output_csv.write('request\tSetSpec\n')  # escreve headers
                            output_csv.write('%s\t%s\n' % (a_set[0], a_set[1]))
                            output_csv.close()                  # fecha csv de output

            except requests.ReadTimeout:                        # tratamento de exceptions
                print 'Connection timeout with %s' % url
                errors.write('Connection timeout with %s\n' % url)
            except requests.exceptions.ConnectionError:
                print 'Connection error with %s\nConnection aborted.' % url
                errors.write('Connection error with %s\n' % url)
            except requests.exceptions.MissingSchema:
                print 'Missing schema on %s\nConnection aborted.' % url
                errors.write('Missing schema on %s\n' % url)
            except requests.exceptions.InvalidSchema:
                print 'No connection adapters found for %s.\n Check url for errors.' % url
                errors.write('Connection error with: %s\n' % url)

    ocurrence_counter = codecs.open('SetNameOcurrences.txt', 'w', 'utf-8-sig')
    for item in setNameList:
        ocurrence_counter.write('%s - %d\n' % (item, setNameList[item]))
    ocurrence_counter.close()
    errors.close()                                          # fecha log de erros
print 'Extraction successfully finished'
