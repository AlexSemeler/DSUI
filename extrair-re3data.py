# -*- coding: utf-8 -*-
"""
Created on Aug 15 2018

@author: Arthur L. Oliveira
"""

import codecs
import requests
import lxml.objectify as obj

record_base = 'https://www.re3data.org/repository/'
repository_list = 'https://www.re3data.org/api/v1/repositories'

html = requests.get(repository_list, timeout=10).content
tree = obj.fromstring('%s' % html)
with codecs.open('RepoListLinks.tsv', 'w', 'utf-8-sig') as records:
    records.write('Link\tName\n')
    for item in tree.getchildren():
        if '\n' not in '%s' % item.name:
            records.write('%s\t%s\n' % (record_base + item.id, item.name))
        else:
            records.write('%s\t%s' % (record_base + item.id, item.name))
records.close()
