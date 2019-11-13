# BuscaSimilaridadeCosseno-Faculdade
## "Interface" de busca por similaridade de cosseno dentro de uma lista de docs
Atividade de Machine Learning - 8ºp


## Introdução
Atividade de "Machine Learning". O objetivo dessa atividade é, a partir de um .csv fornecido pelo user, buscar dentro de todos aqueles dados quais as instâncias tem maior similaridade com o texto procurado, utilizando a técnica de similaridade do cosseno.
1. Obtem um CSV.
2. Utilizando todos as linhas, constrói uma BOW que será utilizada posteriormente
3. Exibe uma ""interface navegável"" que oferece função de buscar dentro da lista de textos, buscar texto único, fornecer um outro parâmetro para ser utilizado como "base para similaridade" e etc 

## Como iniciar o projeto:
Como padrão ele inicialmente procura um arquivo chamado "imdb.jpg"(arquivo baixado a partir de um dataset do kaggle de reviews de filmes <link: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews>), e tem um padrão base de similaridade de 20%
Existem outras importantes:
 - header_line : se o CSV tem uma linha de cabeçalho
 - text_column : qual a coluna que contem o texto no CSV
 - csv_path: endereço do CSV
 - similarity_base: parametro de similaridade aceitável para retorno
----> "csv_path = "imdb.csv", text_column = 2, header_line=True, similarity_base = 0.2" <------

Para executa-lo:
```
python searcher.py
```
## Detalhe importante
# O projeto não contem nenhum CSV, lembre-se de fazer as configurações iniciais
