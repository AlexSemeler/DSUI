# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018

@author: Alexandre Ribas Semeler
@author: Adilson Luiz Pinto
@author: Arthur L. Oliveira
"""

import codecs
import requests
from bs4 import BeautifulSoup
import lxml.objectify as obj
import lxml.etree as etree

xml_error_log = open('xml_errors.txt', 'w')


def get_sets_list(some_url):
    triples_list = []
    html = requests.get(some_url, timeout=10).content
    soup = BeautifulSoup(html, "lxml")
    sets = soup.find_all('set')
    request_url = soup.find('request')
    if 'localhost' in str(request_url) or '127.0.0.1' in str(request_url):
        request_url = some_url.split('?')[0]
    try:
        pure_request_url = obj.fromstring('%s' % request_url)
    except etree.XMLSyntaxError:
        print 'XML syntax error on string: "%s" was the request url' % request_url
        return ''
    for item in sets:
        pair = obj.fromstring('%s' % item)
        triples_list.append([pure_request_url, pair.setspec, pair.setname])
    return triples_list


source = codecs.open('IbictExtract.csv', 'r', 'utf-8-sig')
line_list = source.readlines()
source.close()

with codecs.open('ColectionList.csv', 'w', 'utf-8-sig') as output_csv:
    output_csv.write('request\tSetSpec\tSetName\n')
    with open('error_log.txt', 'w') as errors:
        print 'Begin of extraction:', len(line_list)-2, 'URLs to extract'
        for j in range(1, len(line_list) - 1):
            try:
                url = line_list[j].split('\t')[0]
                print j, ': Extracting from: %s' % url
                set_list = get_sets_list(url)
                if set_list:
                    for a_set in set_list:
                        output_csv.write('%s\t%s\t%s\n' % (a_set[0], a_set[1], a_set[2]))
            except requests.ReadTimeout:
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
    errors.close()
output_csv.close()

print 'Extração Realizada com Sucesso.'
