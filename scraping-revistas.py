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


def get_posts_links(url):

    # Seleciona a secao do site que vai ser coletada
    html = get(url).content
    soup = BeautifulSoup(html, "lxml")
    root = soup.findAll('h3')
    post_list = []
    for item in root:
        link = item.findNext('p').findNext('a')
        while link.getText() != 'Acessar revista':
            link = link.findNext('a')
        post_list.append((item, link))
    return post_list


def extract_data_from_link(post_link):

    # Seleciona relacao dos nomes dos sites e o links
    return {'link': post_link[1].attrs['href'], 'title': post_link[0].getText()}


def create_output_file(data):

    # Salva os dados em um arquivo
    file_path = path.join(path.dirname(__file__), '../Data Science/PeriodicosExtract.csv')
    with open(file_path, 'w', 'utf-8-sig') as output_csv:
        output_csv.write('REPOSITORIO\tFonte de Dados\n')
        for i in data:
            output_csv.write('%soai/request?verb=ListSets\t%s\n' % (i.values()[0], i.values()[1]))


if __name__ == '__main__':

    revistas = open('Revistas.csv', 'r', 'utf-8-sig')
    link_list = revistas.readlines()
    revistas.close()
    data = []

    for i in range(1, len(link_list)):
        posts = get_posts_links(link_list[i].split('\t')[0])

        for post in posts:
            post_data = extract_data_from_link(post)
            print 'Extracting: %s, %s' % (post_data['link'], post_data['title'])

            if post_data:
                data.append(post_data)

    create_output_file(data)
    print 'Pares links->repositórios foram salvos no arquivo ../Data Science/PeriodicosExtract.csv'
