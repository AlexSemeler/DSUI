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
<p>Fase 1 - WEB SCRAPING DE UM SITE FONTE DE LINKS OAI-PMH <br />
  (Site normal, OJS, DSPACE)<br />
  1.1 Copiar todos os links dos repositórios e salvar em um aqruivo .csv.<br />
  1.2 A tabela deve conter as colunas: link e nome do repositório.<br />
  1.3 Testar se o repositório adota o protocolo OAI-PMH<br />
  DSPACE (oai/request?verb=ListSets)<br />
  OJS (/oai/?verb=ListSets) <br />
  1.3 Testar se o repositório adota o protocolo OAI-PMH.<br />
  Ex: Tabela em csv com a relação de todos os repositórios é salva <br />
  Scripts <br />
  DSpace:<br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/scraping-ibict.py">https://github.com/AlexSemeler/DSUI/blob/master/scraping-ibict.py</a><br />
  OJS – Portais <br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/scraping-revistas.py">https://github.com/AlexSemeler/DSUI/blob/master/scraping-revistas.py</a><br />
  + csv com lista de links dos portais <br />
  CSV RESULTADO DA BUSCA (OJS) <br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/colecoes.csv">https://github.com/AlexSemeler/DSUI/blob/master/colecoes.csv</a><br />
  ==============================================<br />
  Fase 2 - WEB SCRAPING DAS COLEÇÕES EM CADA REPOSITÓRIO<br />
  2.1 Executar a expressão de busca: nomedorepositorio/oai/request?verb=ListSets,  para visualizar a relação de coleções de cada repositório lendo o CSV RESULTADO  DA BUSCA.( <a href="https://github.com/AlexSemeler/DSUI/blob/master/colecoes.csv">https://github.com/AlexSemeler/DSUI/blob/master/colecoes.csv</a>) <br />
  2.2 Converter a request acima de XML  para CSV. <br />
  2.3 A tabela csv deve conter colunas com: o request, setspec e setname de cada  uma das coleções dos repositórios.<br />
  Script <br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/coleta_nome_colecoes.py">https://github.com/AlexSemeler/DSUI/blob/master/coleta_nome_colecoes.py</a><br />
  Resultado CSV<br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/CollectionPeriodicosList.csv">https://github.com/AlexSemeler/DSUI/blob/master/CollectionPeriodicosList.csv</a><br />
  ======================================================<br />
  Fase 3 – Limpeza do nome dos SetNames<br />
  Resultado CSV – OJS<br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/CollectionPeriodicosList.csv">https://github.com/AlexSemeler/DSUI/blob/master/CollectionPeriodicosList.csv</a><br />
  Resultado DSpace <a href="https://github.com/AlexSemeler/DSUI/blob/master/ColectionListCSV.csv">https://github.com/AlexSemeler/DSUI/blob/master/ColectionListCSV.csv</a><br />
  3.1 Verificar erros de ortografia, digitação e faz agrupamento por ocorrência  de palavras. <br />
  3.2 Salvar ocorrências de palavras e gerar um .csv por assunto.<br />
  3.2 Selecionar coleções por assunto<br />
  <a href="https://github.com/AlexSemeler/DSUI/edit/master/CSVDivideAndConstruct.py">https://github.com/AlexSemeler/DSUI/edit/master/CSVDivideAndConstruct.py</a><br />
  <strong>+ csv resultado da fase 2 </strong><br />
  Fase 4 - HARVESTING DE METADADOS<br />
  <br />
  4.1 Executar o script pyoaiharvest.py + Listcolecao.csv .<br />
  4.2 Coletar e salvar os metadados das coleções em XML e salvar em um diretório  com o nome do assunto. <br />
  Fase 5 - CONVERTER AS COLEÇÕES XML PARA UM ÚNICO .CSV<br />
  5. 1 Executar o script converter-xml-csv.py<br />
  OJS <br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/revista-xml-csv-converter.py">https://github.com/AlexSemeler/DSUI/blob/master/revista-xml-csv-converter.py</a><br />
  Dspace <br />
  <a href="https://github.com/AlexSemeler/DSUI/blob/master/converte-xml-csv.py">https://github.com/AlexSemeler/DSUI/blob/master/converte-xml-csv.py</a><br />
</p>
