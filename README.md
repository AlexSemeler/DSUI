<p># DSUI </p>
<p>Data Science em Unidades de Informação - Modulo da Disciplina: Estudos Métricos em Informação <br />
  Projeto vinculado ao estágio pós-doutoral Pnpd/CAPES junto ao PGCIN-UFSC</p>
<p>Autor: Alexandre Ribas Semeler<br />
  Supervisão: Adilson Luiz Pinto<br />
  Bolsista de Computação: Arthur L. Oliveira<br />
  ------------------------------<br />
  Objetivo: Explorar técnicas de Coleta, Manipulação e e Visualização de Metadados dos Repositórios Institucionais Brasileiros <br />
  para criação de um serviços de avaliação e monitoramento de produção científica nacional<br />
  ------------------------------<br />
  Requisitos:</p>
<p>Open Refine<br />
  Python 2.7<br />
  Open Oficce<br />
  Site IBICT<br />
  ------------------------------<br />
  Metas:<br />
  a) descartar dados de referência e serviços de citação extraídos de bases de dados internacionais proprietárias e/ou comerciais<br />
  como Web of Science da Thompson Scientific, Scopus, Elsevier e etc. <br />
  b) priorizar metadados publicados na web por universidades e ou institutos de pesquisa no Brasil;<br />
  c) representar metadados de coleções de artigos, dissertações e teses;<br />
  d) automatizar os processos metodológicos via scripts em Python e softwres de manipulação de dados (open Refine);<br />
  e) reunir conteúdo extraído de diversas fontes para formar uma coleção temática</p>
<p>Processo de Pesquisa </p>
<p>Fase 1 - WEB SCRAPING SITE IBICT<br />
  <br />
  1.1 Copiar todos os links dos repositórios institucionais brasileiros que estão disponíveis no site IBICT e salvar em um aqruivo .csv. <br />
  Ex: Script para copiar a relação de links do IBICT<br />
  1.2 A tabela deve conter as colunas: link e nome do repositório.<br />
  1.3 Testar se o repositório adota o protocolo OAI-PMH. Para isso utilize a espressão: oai/request?verb=ListSets, ao final dos endereços dos repositórios.<br />
  Ex:  Tabela em csv com a relação de todos os repositórios brasileiros<br />
  <br />
  Fase 2 - WEB SCRAPING DAS COLEÇÕES EM CADA REPOSITÓRIO<br />
  <br />
  2.1 Executar a espressão de busca: nomedorepositorio/oai/request?verb=ListSets, para visualizar a relação de coleções de cada repositório.<br />
  2.2 Converter a request acima de XML para CSV. <br />
  Ex: Script para executar () para salvar as coleções com o resultado da espressão de busca: nomedorepositorio/oai/request?verb=ListSets<br />
  2.3 A tabela csv deve conter colunas com: o request, setspec e setname de cada uma das coleções dos repositórios. <br />
  Ex: Tabela em csv com resultado da coleta de todas as coleções disponíveis nos repositórios brasileiros<br />
  <br />
Fase 3 - DATA HANDLING COM OPEN REFINE <br />
<br />
  3.1 Verificar erros de ortográfia, digitação e selecionar coleções por assunto.<br />
Ex: Ver tutorial Open Refine <br />
<br />
Fase 4 - HARVESTING DE METADADOS<br />
<br />
  3.1 Executar o script pyoaiharvest.py + Listcolecao.csv .<br />
  3. 2 Coletar e salvar os metadados das coleções em XML. <br />
  <br />
  Fase 5 
  - CONVERTER  AS COLEÇÕES XML PARA UM ÚNICO .CSV<br />
</p>
<p>5. 1 Executar o script converter-xml-csv.py<br />
  <br />
  Fase 6 - DATA HANDLING COM OPEN REFINE <br />
  <br />
  5.1 Verificar erros de ortográfia, digitação e selecionar coleções por assunto.<br />
Ex: Ver tutorial Open Refine </p>
