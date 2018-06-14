# DSUI 

Data Science em Unidades de Informação - Modulo da Disciplina: Estudos Métricos em Informação 
Projeto vinculado ao estágio pós-doutoral Pnpd/CAPES junto ao PGCIN-UFSC

Autor: Alexandre Ribas Semeler
Supervisão: Adilson Luiz Pinto
Bolsita de Computação: Arthur L. Oliveira
------------------------------
Objetivo: Explorar técnicas de Coleta, Manipulação e e Visualização de Metadados dos Repositórios Institucionais Brasileiros 
para criação de um serviços de avaliação e monitoramento de produção científica nacional
------------------------------
Requisitos:

Open Refine
Python 2.7
Open Oficce
Site IBICT
------------------------------
Metas:
a) descartar dados de referência e serviços de citação extraídos de bases de dados internacionais proprietárias e/ou comerciais
como Web of Science da Thompson Scientific, Scopus, Elsevier e etc. 
b) priorizar metadados publicados na web por universidades e ou institutos de pesquisa no Brasil;
c) representar metadados de coleções de artigos, dissertações e teses;
d) automatizar os processos metodológicos via scripts em Python e softwres de manipulação de dados (open Refine);
e) reunir conteúdo extraído de diversas fontes para formar uma coleção temática

Processo de Pesquisa 

Fase 1 - WEB SCRAPING SITE IBICT
1.1 Copiar todos os links dos repositórios institucionais brasileiros que estão disponíveis no site IBICT e salvar em um aqruivo .csv. 
      Ex: Script para copiar a relação de links do IBICT
1.2 A tabela deve conter as colunas: link e nome do repositório.
1.3 Testar se o repositório adota o protocolo OAI-PMH. Para isso utilize a espressão: oai/request?verb=ListSets, ao final dos endereços dos repositórios.
     Ex:  Tabela em csv com a relação de todos os repositórios brasileiros
Fase 2 - WEB SCRAPING DAS COLEÇÕES EM CADA REPOSITÓRIO
2.1 Executar a espressão de busca: nomedorepositorio/oai/request?verb=ListSets, para visualizar a relação de coleções de cada repositório.
2.2 Converter a request acima de XML para CSV. 
    Ex: Script para executar () para salvar as coleções com o resultado da espressão de busca: nomedorepositorio/oai/request?verb=ListSets
2.3 A tabela csv deve conter colunas com: o request, setspec e setname de cada uma das coleções dos repositórios. 
     Ex: Tabela em csv com resultado da coleta de todas as coleções disponíveis nos repositórios brasileiros
2 DATA HANDLING COM OPEN REFINE 
2.1 Verificar erros de ortográfia, digitação e selecionar coleções por assunto.
    Ex: Ver tutorial Open Refine 
3 HARVESTING DE METADADOS
3.1 Executar o script pyoaiharvest.py + Listcolecao.csv .
3. 2 Coletar e salvar os metadados das coleções em XML. 
4 CONVERTER  AS COLEÇÕES XML PARA UM ÚNICO .CSV
   4. 1 Executar o script converter-xml-csv.py
5 DATA HANDLING COM OPEN REFINE 
5.1 Verificar erros de ortográfia, digitação e selecionar coleções por assunto.
  Ex: Ver tutorial Open Refine 

