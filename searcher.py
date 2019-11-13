import math
import csv
import time
import os


class searcher(object):
    
    text_list = []

    def __init__(self, csv_path = "imdb.csv", text_column = 2, header_line=True, similarity_base = 0.2):
        self.csv_path = csv_path
        self.header_line = header_line
        self.text_column = text_column
        self.similarity_base = similarity_base
        self.bag_of_words = []
        self.words_list_qtd = {}

    def run(self):
        text_list = self.get_text_list()
        self.text_list = text_list
        self.prepare_searcher(text_list)
        self.main_program()
    
    def main_program(self):
        menu = """###      P Y O G L E E  S E A R C H E R         ###\n| Bem vindo ao menu do Pyoglee\n| 1 - Buscar uma palavra ou frase no banco\n| 2 - Exibir algum documento único(busca única)\n| 3 - Exibir alguns exemplos de textos do banco\n| 4 - Alterar o número base de similaridade aceitavel\n| 5 - Finalizar o programa\n###################################################\n"""
        while (True):
            player_input = input(menu)
            if player_input == "1":
                # Buscar uma palavra ou frase no banco 
                self.search()
            elif player_input == "2":
                # Buscar um unico documento
                doc_name = input("Por favor, digite o nome do documento\n>> ")
                print(self.get_document(doc_name))
            elif player_input == "3":
                # Exibir alguns exemplos de textos do banco
                for d in self.text_list[:10]:
                    print("[{}]".format(d))
            elif player_input == "4":
                # Mudar o parametro de valor base de comparacao
                self.similarity_base = float(input("Por favor, digite um número de 0 a 1 ~ (Sem validação)\n>> "))
            elif player_input == "5":
                # Finalizar o programa
                break
            else:
                print("Opção inválida, favor selecionar as opções do menu")
            print("\n")

    def search(self):
        text_display = """Qual a palavra/frase você deseja procurar?\n>> """
        text = input(text_display)
        text_word_list = self.build_word_list_qtd(text.lower())
        r_list = []
        for t_position in range(len(self.words_list_qtd)):
            doc = "doc{}".format(t_position)
            r = self.cosine_similarity(text_word_list, doc)
            if r[1] > self.similarity_base:
                r_list.append(r)
        r_list.sort(key=lambda x: x[1], reverse=True)
        for r in r_list[:20]:
            print("{}.".format(r[0]))

        if not len(r_list) > 0:
            print(
                "\n Nenhuma similaridade encontrada de acordo com os padrões instaurados de base de similaridade: {}\n".format(self.similarity_base))

    def get_document(self, doc):
        pos = doc.replace("doc", "")
        try:
            pos = int(pos)
            return "[{}]".format(self.text_list[pos])
        except:
            print("Problema em buscar {} - > posicao {}".format(doc, pos))

    def prepare_searcher(self, text_list):
        start = time.time()
        for text in text_list:
            self.words_extract(text)

        # Filtra todas as palavras que sao maiores que 3 caracteres
        self.bag_of_words = list(filter(lambda x: len(x) > 3, self.bag_of_words))

        for text in text_list:
            doc_key = "doc{}".format(len(self.words_list_qtd))
            self.words_list_qtd.update(
                {
                    doc_key : self.build_word_list_qtd(text.lower())
                }
            )
        end = time.time()
        print("Tempo de execução da preparação é de é de: {}".format(str(end - start)))

    def cosine_similarity(self, text_word_list, text2):
        doc1_values = text_word_list
        doc2_values = self.words_list_qtd[text2]
        try:
            result = self.summation_method(doc1_values, doc2_values) / (
                math.sqrt(self.summation_method(doc1_values)) * math.sqrt(self.summation_method(doc2_values)))
        except:
            result = 0
        text = "Similaridade de {} e {} é de {}".format("Busca", text2, round(result, 4))
        
        return (text, result)

    def build_word_list_qtd(self,text):
        return [text.count(word) for word in self.bag_of_words]

    def words_extract(self, text):
        word = ""
        for c in text.lower():
            if c.isalnum():
                word += c
            else:
                if word and not word in self.bag_of_words:
                    self.bag_of_words.append(word)
                word = "" 
        self.bag_of_words.append(word)

    def get_text_list(self):
        list = []
        with open(self.csv_path, mode='r', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 and self.header_line:
                    line_count = 1
                else:
                    list.append(row[self.text_column])                   
        return list

    @staticmethod
    def summation_method(lista1, lista2=[]):
        soma = 0
        if lista2 == []:
            for i in range(len(lista1)):
                aux = lista1[i] ** 2
                soma += aux
        else:
            for i in range(len(lista1)):
                soma += lista1[i] * lista2[i]
        return soma


if __name__ == "__main__":
    s = searcher()
    s.run()