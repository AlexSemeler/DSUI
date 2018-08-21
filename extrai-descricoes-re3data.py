# -*- coding: utf-8 -*-
"""
Created on Aug 15 2018

@author: Arthur L. Oliveira
"""

import codecs
import requests
import lxml.objectify as obj


def extract_item(field, item, a_tuple, index, namespace):
    if namespace + field == item.tag:
        a_tuple[index] = item
        return True
    return False


def extract_list_item(field, item, a_tuple, index, namespace):
    if namespace + field == item.tag:
        a_tuple[index].append(item)
        return True
    return False


with codecs.open('RepoListAPI.tsv', 'r', 'utf-8-sig') as api_file:
    link_list = api_file.readlines()
    api_file.close()

with codecs.open('Re3Data_repositories2.tsv', 'w', 'utf-8-sig') as reps:
    namespaces = {'r3d': ''}
    reps.write('Name\tDescription\tURL\tSoftware Name\tLicense\tData Acess Type\t'
               'Rep. Type\tContent Type\tRep. Language\tInstitution\tCountry\tInst. Type\tKeyword\tSubject\n')
    print 'PARSING START, %d repositories listed' % len(link_list)
    for i in range(1, len(link_list) - 1):
        try:
            html = requests.get(link_list[i].split('\t')[0], timeout=10).content
        except requests.ConnectTimeout:
            print 'Connection timeout with %s Parsing aborted.' % link_list[i]
            continue
        except requests.exceptions.SSLError:
            print 'SSL error with %s Parsing aborted.' % link_list[i]
            continue
        tree = obj.fromstring('%s' % html)
        namespaces['r3d'] = tree.tag.split('}')[0] + '}'
        tree = tree.repository
        writing_tuple = [0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], []]
        print 'PARSING: %d from %d' % (i, len(link_list))
        for child in tree.getchildren():
            if extract_item('repositoryName', child, writing_tuple, 0, namespaces['r3d']):
                continue
            # if extract_item('description', child, writing_tuple, 1, namespaces['r3d']):
            #    continue
            if extract_item('repositoryURL', child, writing_tuple, 2, namespaces['r3d']):
                continue
            if namespaces['r3d'] + 'software' == child.tag:
                writing_tuple[3] = child.softwareName
                continue
            if namespaces['r3d'] + 'dataLicense' == child.tag:
                writing_tuple[4] = child.dataLicenseName
                continue
            if namespaces['r3d'] + 'dataAccess' == child.tag:
                writing_tuple[5] = child.dataAccessType
                continue
            if extract_list_item('type', child, writing_tuple, 6, namespaces['r3d']):
                continue
            if extract_list_item('contentType', child, writing_tuple, 7, namespaces['r3d']):
                continue
            if extract_list_item('repositoryLanguage', child, writing_tuple, 8, namespaces['r3d']):
                continue
            if namespaces['r3d'] + 'institution' == child.tag:
                writing_tuple[9].append(child.institutionName)
                writing_tuple[10].append(child.institutionCountry)
                writing_tuple[11].append(child.institutionType)
                continue
            if extract_list_item('keyword', child, writing_tuple, 12, namespaces['r3d']):
                continue
            if extract_list_item('subject', child, writing_tuple, 13, namespaces['r3d']):
                continue
        for j in range(0, 6):
            reps.write('%s'.translate(None, '\t\n') % writing_tuple[j] + '\t')
        for j in range(6, len(writing_tuple)):
            limit = len(writing_tuple[j])
            for k in range(0, limit):
                if k < limit - 1:
                    reps.write('%s, '.translate(None, '\t\n') % writing_tuple[j][k])
                else:
                    if j < len(writing_tuple) - 1:
                        reps.write('%s'.translate(None, '\t\n') % writing_tuple[j][k] + '\t')
                    else:
                        reps.write('%s'.translate(None, '\t\n') % writing_tuple[j][k] + '\n')
    reps.close()
print 'WRITING ENDED, output file shall have %d lines.' % len(link_list)
