# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:14:45 2016
Edited on Wed May 23 16:43:00 2018

@author: alexandresemeler
@author: Arthur L. Oliveira
"""

from os import path
from codecs import open
from requests import get
from bs4 import BeautifulSoup


def get_posts_links(url):               # Recebe uma url como parametro

    html = get(url).content             # extrai o conteudo para a variavel 'html'
    soup = BeautifulSoup(html, "lxml")  # cria variavel para o parsing do conteudo da pagina
    root = soup.findAll('h3')           # root <- lista de linhas onde 'h3' ocorre
    post_list = []                      # cria lista vazia para preencher com os links
    for item in root:
        link = item.findNext('p').findNext('a')     # link <- proxima ocorrencia de 'p' seguido de 'a'
        while link.getText() != 'Acessar revista':  # enquanto o texto na linha do link não for 'acessar revista'
            link = link.findNext('a')               # link <- a proxima ocorrencia de 'a'
        post_list.append((item, link))              # inclui um par (nome, link) na lista
    return post_list                                # retorna a lista


def extract_data_from_link(post_link):
    # retorna um par (link, name)
    return {'link': post_link[1].attrs['href'], 'title': post_link[0].getText()}


def create_output_file(some_data):
    # Salva os dados em um arquivo csv
    file_path = path.join(path.dirname(__file__), '../Data Science/output_files/PeriodicosExtract.csv')
    with open(file_path, 'w', 'utf-8-sig') as output_csv:
        output_csv.write('REPOSITORIO\tFonte de Dados\n')   # escreve headers do csv
        for item in some_data:                              # completa urls a serem escritas e as escreve junto com nome
            output_csv.write('%s/oai/?verb=ListSets\t%s\n' % (item.values()[0], item.values()[1]))


if __name__ == '__main__':

    try:
        # csv com lista de collections para leitura
        revistas_path = path.join(path.dirname(__file__), '../Data Science/dados/Revistas.csv')
        revistas = open(revistas_path, 'r', 'utf-8-sig')
    except IOError:
        print 'File Revistas.csv not found, extraction aborted'
    else:
        link_list = revistas.readlines()                        # bufferiza csv em lista na RAM
        revistas.close()                                        # fecha csv
        data = []                                               # inicializa lista vazia para preencher com dados
        counter = 0
        for index in range(1, len(link_list)):                          # percorre lista de revistas
            posts = get_posts_links(link_list[index].split('\t')[0])    # posts <- lista de pares (nome, link)

            for post in posts:                                          # percorre 'posts' e prepara 'post_data'
                post_data = extract_data_from_link(post)                # post_data <- um par (link, name)
                if post_data:                                           # trata par caso ele seja diferente de vazio
                    if not data or post_data['link'] != data[-1]['link']:
                        counter += 1
                        print '%d Extracting: %s, %s' % (counter, post_data['link'], post_data['title'])
                        data.append(post_data)                          # inclui par na lista 'data' caso esteja correto
                    elif post_data['link'] == data[-1]['link']:
                        # informa que nome foi corrigido em caso de erros no nome
                        print "Title correction: '%s' is actually '%s'" % (data[-1]['title'], post_data['title'])
                        data[-1]['title'] = post_data['title']

        create_output_file(data)                                        # gera arquivo csv de output

print 'Pares links->repositórios foram salvos no arquivo ../Data Science/output_files/PeriodicosExtract.csv'
