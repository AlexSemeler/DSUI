
# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018

@author: Alexandre Ribas Semeler
@author: Arthur L. Oliveira
"""


import codecs #para abrir arquivo final com utf8
import os     #para encontrar os arquivos usando o sistema
import glob   #usado junto com "os" para montar o caminho a ser percorrido para a pasta alvo
import lxml.objectify as obj #para transformar o xml lido em um objeto de melhor manuseio depois do parsing
import lxml.etree #usado para tratar as exceptions de parsing

path = '../dados/geo-repositorios/'                              #caminho do sistema operacional para a pasta alvo
output_file = codecs.open('../dados/csv/amostra-repositorios-geociencias.csv','w','utf-8-sig')    #output_file <- um arquivo a ser escrito
output_file.write('date\ttitle\tidentifier\ttype\tcreators\tsubjects\n')        #inicializa headers do arquivo
reg_counter = 0                                             #inicializa contador de registros

for filename in glob.glob(os.path.join(path, '*.xml')):     #para cada arquivo na pasta apontada por path
    print('parsing %s' %filename.split('\\')[-1])
    
    try:                                                    #try utilizado para prevenir runtime errors
        with open(filename, 'r') as f:                      #f <- um arquivo xml
            tree = obj.fromstring(f.read())                 #tree <- f após parsing        
            f.close()                                       #fecha o arquivo f após terminar leitura para a RAM
            
            for i in tree.record:                           #percorre todos os records do arquivo
                for j in i.metadata.getchildren():          #percorre os campos internos de cada record
                    metadata_list = j.getchildren()         #inicializa lista com metadados do record
                    output_tuple = [0,0,0,0,[],[]]            #inicializa a tupla de escrita
                    
                    for item in metadata_list:              #preenche a tupla a ser escrita no arquivo
                        if 'date' in item.tag:
                            if len(str(item).split('-')[0]) == 4:
                                output_tuple[0] = str(item).split('-')[0]
                            continue
                        if 'title' in item.tag:
                            output_tuple[1] = item
                            continue
                        if 'identifier' in item.tag:
                            output_tuple[2] = item
                            continue
                        if 'type' in item.tag:
                            output_tuple[3] = item
                            continue
                        if 'creator' in item.tag:
                            output_tuple[4].append(item)
                            continue
                        if 'subject' in item.tag:              
                            output_tuple[5].append(item)    #tupla <- [title, identifier, type, [creators], [subjects]]
                            continue
                    
                    if output_tuple[0] != 0:                #escreve date na linha atual do arquivo caso exista
                        output_file.write('%s\t' %output_tuple[0])
                    else:
                        output_file.write('No date\t')      #caso nulo: escreve aviso
                    
                    if output_tuple[1] != 0:                #escreve title no arquivo caso exista
                        output_file.write('%s\t' %output_tuple[1])  
                    else:
                        output_file.write('No title\t')     #caso title seja 0: escreve aviso
            
                    if output_tuple[2] != 0:                #escreve identifier no arquivo caso exista
                        output_file.write('%s\t' %output_tuple[2])
                    else:                                   #caso identifier seja 0: escreve aviso
                        output_file.write('No identifier\t')
                        
                    if output_tuple[3] != 0:                #escreve type no arquivo caso exista
                        output_file.write('%s\t' %output_tuple[3])
                    else:
                        output_file.write('No type\t')      #caso type seja 0: escreve aviso
                    
                    if output_tuple[4] != []:               #verifica se existe lista de creators
                        for m in output_tuple[4]:           #escreve creators no arquivo
                            if m == output_tuple[4][-1]:
                                output_file.write('%s\t' %m)
                            else:
                                output_file.write('%s, ' %m)
                    else:
                        output_file.write('No creators\t')  #caso lista seja vazia: escreve aviso
                        
                    if output_tuple[5] != []:               #verifica se existe lista de subjects                            
                        for n in output_tuple[5]:           #escreve subjects no arquivo
                            if n == output_tuple[5][-1]:
                                output_file.write('%s' %n)  #escreve o ultimo elemento sem \t pois a linha acaba
                            else:
                                output_file.write('%s, ' %n)
                    else:
                        output_file.write('No subjects')    #caso lista seja vazia: escreve aviso
                        
                    output_file.write('\n')                 #termina de escrever a tupla no arquivo e vai para a proxima linha
                    reg_counter += 1
                    
    except lxml.etree.LxmlSyntaxError:                      #informa se um arquivo estiver corrompido
        print('file "%s" corrupted: parsing aborted' %filename.split('\\')[-1])
    except:
        pass                                                #garante integridade do programa mesmo com erros
        
output_file.close()                                         #fecha arquivo ao final do programa
print 'aprox.', reg_counter,'rows on output file'           #informa quantos registros foram escritos
