# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:14:45 2016
Edited on Wed May 23 16:43:00 2018

@author: Alexandre Ribas Semeler
@author: Adislon Luiz Pinto 
@author: Arthur L. Oliveira
"""
from os import path
from codecs import open
from requests import get
from bs4 import BeautifulSoup

print 'Coleta dos Links relativos a lista de Repositórios Institucionais Brasileiros disponíveis no site do IBICT\n'
url = "http://www.ibict.br/informacao-para-ciencia-tecnologia-e-inovacao%20/repositorios-digitais/repositorios-brasileiros"
    # funcao que seleciona as tags do site do ibict que vão ser coletadas
def get_posts_links():
    html = get(url).content
    soup = BeautifulSoup(html, "lxml")
    return soup.findAll('a', {'class': 'external-link'})

# função que seleciona as links do site do ibict que vão ser coletados
def extract_data_from_link(post_link_tag):

    # Seleciona relacao dos nomes dos sites e o links
    return {'link': post_link_tag.attrs['href'], 'title': post_link_tag.getText()}

# função que cria o csv com nome do repositorio e o link 
def create_output_file(data):

   # função que salva os dados em um arquivo csv e acrescenta o request OAI-PMH
    file_path = path.join(path.dirname(__file__), '../dados/csv/IbictwebExtract.csv')
    with open(file_path, 'w', 'utf-8-sig') as output_csv:
        output_csv.write('REPOSITORIO\tFonte de Dados\tGood?\n')
        for i in data:
            output_csv.write('%soai/request?verb=ListSets\t%s\tYES\n' % (i.values()[0], i.values()[1]))


if __name__ == '__main__':
    posts = get_posts_links()
    data = []

    for post in posts:
        post_data = extract_data_from_link(post)
        data.append(post_data)

    create_output_file(data)
    print 'Os links foram salvos  no arquivo ../dados/IbictwebExtract.csv'
