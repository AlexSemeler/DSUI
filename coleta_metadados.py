# -*- coding: utf-8 -*-
"""
Created on Apr 15 2018
@author: Alexandre Ribas Semeler
@author: Adilson Luiz Pinto
@author: Arthur L. Oliveira
"""
import os
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# arquivo em csv contendo a de colecões a serem coletadas 
lista = pd.read_csv('../dados/csv/direito.csv') # modificar o nome do arquivo 

########################################################
#seleciona os dados contendo links, nome e Setcspec que vao ser coletados em uma planilha csv 
def busca(request=None,SetSpec=None,SetName=None):
  print "Comando executado no terminal para extracao da colecao:"
  print "python pyoaiharvest.py -l",request, "-o", SetSpec,".dc.xml -s"
  print "A colecao extraida foi:", SetName
  
#Executa o script  pyoaiharvest.py para coletar os metadados
#lê o csv contendo (link SetSpec SetName)
  os.system("python pyoaiharvest.py -l {0} -o ../dados/direito/{1}.dc.xml -s {1}".format(request, SetSpec,))# modificar o caminho onde os XMLs serão salvos
  
for i in range(len(lista)-1):
    busca(lista['request'][i], lista['SetSpec'][i], lista['SetName'][i])
print 'Coleta Concluída'
#Salva a coleta em arquivos XML (link SetSpec SetName)
