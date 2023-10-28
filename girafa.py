import time
from random import choice

class Girafa:
    # Propriedades
    nome
    altura
    idade
    cor
    origem

    # O método __init__ é executado quando a classe é instanciada

    def __init__(self, nome, altura, idade, cor, origem):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.cor = cor
        self.origem = origem
        self.__fome = 100
    
    def andar(self):
        if self.__fome > 60:
            print(self.nome, "não pode andar porque está morrendo de fome")
        else:
            print(self.nome, "está andando..")

    def comer(self, alimento):
        lista_alimentos = ['folhas', 'frutas', 'plantas']

        if alimento in lista_alimentos:
            self.__fome -= 10
        else:
            print(self.nome, "não come esse tipo de coisa...")
    
    def fome(self):
        if self.__fome > 60:
            print(self.nome, "Está morrendo de fome!")
        elif self.__fome > 40:
            print(self.nome, "Está com fome!")
        elif self.__fome > 20:
            print(self.nome, "Está saciada.")
        elif self.__fome > 0:
            print(self.nome, "Está cheia.")
        elif self.__fome > 0:
            print(self.nome, "Está explodindo.")

    def respirar(self):
        print(self.nome, "Inspira..")
        time.sleep(2)
        print(self.nome, "Esxpira..")

    # Função para reproduzir girafas, elas recebe um parceiro e retorna um filhote
    def reproduzir(self, parceiro):
        if not isinstance(parceiro, Girafa):
            print(self.nome, "sai correndo desesperado")
        
        nome = "Filhote de " + self.nome
        altura = (self.altura + parceiro.altura) / 2
        idade = 1
        cor = choice([self, parceiro]).cor
        origem = self.origem

        filhote = Girafa(nome, altura, idade, cor, origem)
        return filhote
