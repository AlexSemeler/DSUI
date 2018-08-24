"""
created on Aug 24 2018
@author: Arthur L. Oliveira
"""

from codecs import open
from os import path
from glob import glob


def my_translate(a_string, char_list):
    for char in char_list:
        a_string = a_string.replace(char, '')
    return a_string


ris_folder = 'RIS-SABI'                               # caminho do sistema para a pasta de ris
output_file = open('SABI_RIS_LIST.tsv', 'w', 'utf-8-sig')
output_file.write('Year\tTitle\tLanguage\tPublisher\tDOI\tISBN/ISSN\ttype\tAuthors\tKeywords\n')
headers_dict = {'PY': 0, 'TI': 1, 'LA': 2, 'PB': 3, 'DO': 4, 'SN': 5, 'TY': 6}
headers_list_dict = {'AU': 7, 'KW': 8}
table = '\t\n\r'

for filename in glob(path.join(ris_folder, '*.ris')):                   # percorre a pasta apontada por path
    a_ris = open(filename, 'r', 'utf-8-sig')                            # abre os arquivos ris um a um
    line_list = a_ris.readlines()
    a_ris.close()
    tuple_list = []
    writing_tuple = [None, None, None, None, None, None, None, [], []]

    for line in line_list:
        if line[:2] in headers_dict:
            writing_tuple[headers_dict[line[:2]]] = '%s' % my_translate(line[6:], table)
            continue
        if line[:2] in headers_list_dict:
            writing_tuple[headers_list_dict[line[:2]]].append('%s' % my_translate(line[6:], table))
            continue
        if line[:2] == 'ER':
            tuple_list.append(writing_tuple)
            writing_tuple = [None, None, None, None, None, None, None, [], []]

    for a_tuple in tuple_list:
        for index in range(7):
            if a_tuple[index]:
                output_file.write('%s\t' % a_tuple[index])
            else:
                output_file.write('Not found\t')

        for index in range(7, len(a_tuple)):
            if a_tuple[index]:
                for item in a_tuple[index][:-1]:
                    output_file.write('%s, ' % item)
                output_file.write('%s' % a_tuple[index][-1])
                if index < len(a_tuple) - 1:
                    output_file.write('\t')
                else:
                    output_file.write('\n')
            else:
                output_file.write('Not found')
                if index < len(a_tuple) - 1:
                    output_file.write('\t')
                else:
                    output_file.write('\n')

output_file.close()

