class Girafa:
    # Propriedades


    # O método __init__ é executado quando a classe é instanciada

    def __init__(self, nome, altura, idade, cor, origem):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.cor = cor
        self.origem = origem
    
    def andar(self):
        print(self.nome, "está andando..")

    def comer(self):
        print(self.nome, "está comendo..")
    
    def respirar(self):
        print(self.nome, "está viva..")
    
    def reproduzir(self):
        print(self.nome, "está acasalando..")