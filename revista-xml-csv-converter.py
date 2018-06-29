# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018
@author: Alexandre Ribas Semeler
@author: Adilson Luiz Pinto
@author: Arthur L. Oliveira
"""

from codecs import open
from os import path
from glob import glob
import lxml.objectify as obj
import lxml.etree as xml_tree


def test_to_write(a_list, list_index, a_file, header_list):
    if a_list[list_index] != 0:
        a_file.write('%s\t' % a_list[list_index])
    else:
        a_file.write('No %s\t' % header_list[list_index])


def test_to_write_list(a_list, list_index, a_file, header_list):
    if a_list[list_index]:
        for k in a_list[list_index]:
            if k != a_list[list_index][-1]:
                a_file.write('%s, ' % k)
                continue
            a_file.write('%s\t' % k)
    else:
        a_file.write('No %s\t' % header_list[list_index])


xml_folder = '../Data Science/dados/revistas'                               # caminho do sistema para a pasta de xmls
aux_header_list = ['date', 'title', 'language', 'publisher', 'format',
                   'identifier', 'rights', 'source', 'type', 'creator', 'subject']
output_file = open('output_tuples_revistas.csv', 'w', 'utf-8-sig')          # abre novo arquivo csv para escrita
# headers do CSV
output_file.write('date\ttitle\tlanguage\tpublisher\tformat\tidentifier\trights\tsource\ttype\tcreator\tsubject\n')
xml_record_counters = {}                                    # instancia um dict para os contar registros em cada xml

for filename in glob(path.join(xml_folder, '*.xml')):                   # percorre a pasta apontada por path

    short_name = filename[:].split('\\')[-1].replace('.dc.xml', '')     # auxiliar para o nome dos arquivos
    xml_record_counters[short_name] = 0                         # inicializa lista de contadores de registro dos xml
    print('parsing: %s' % short_name)

    an_xml = open(filename, 'r')                    # abre os arquivos xml um a um
    try:                                            # try utilizado para prevenir parada por erros no arquivo
        tree = obj.fromstring(an_xml.read())        # tree <- xml após parsing
        an_xml.close()                              # fecha o xml após parsing
    except xml_tree.LxmlSyntaxError:                # informa se o xml estiver corrompido
        print('file "%s" corrupted: parsing aborted' % short_name)
        an_xml.close()                              # fecha o xml após parsing
        continue

    try:
        for record in tree.record:
            for element in record.metadata.getchildren():  # método getchildren evita o uso dos namespaces

                writing_tuple = [0, 0, 0, 0, 0, 0, 0, 0, 0, [], []]    # inicializa a tupla de escrita

                for item in element.getchildren():
                    if 'date' in item.tag:
                        if len(str(item).split('-')[0]) == 4:
                            writing_tuple[0] = str(item).split('-')[0]
                        continue
                    if 'creator' in item.tag:
                        writing_tuple[9].append(item)
                        continue
                    if 'subject' in item.tag:
                        writing_tuple[10].append(item)
                        continue
                    for index in range(1, 8):
                        if aux_header_list[index] in item.tag:
                            writing_tuple[index] = item
                            break
                    continue
                    # tupla preenchida em seus 11 campos

                for i in range(0, 8):
                    test_to_write(writing_tuple, i, output_file, aux_header_list)

                test_to_write_list(writing_tuple, 9, output_file, aux_header_list)
                test_to_write_list(writing_tuple, 10, output_file, aux_header_list)
                output_file.write('\n')                     # quebra linha ao final da escrita no CSV
                xml_record_counters[short_name] += 1        # incrementa contador de registros do xml aberto

    except AttributeError:                                  # informa se o xml estiver sem records
        print('file "%s" apparently got no records: parsing aborted' % short_name)

output_file.close()                                                         # fecha arquivo ao final do programa
print 'aprox.', sum(xml_record_counters.values()), 'rows on output file'    # informa quantos registros foram escritos
