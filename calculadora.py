class Calculadora:

    def __init__(self):
        self.chamar_numero()
    
    def somar(self):
        soma = (self.numero_um + self.numero_dois)
        return soma

    def subtrair(self):
        subtracao = (self.numero_um - self.numero_dois)
        return subtracao    

    def multiplicar(self):
        multiplicacao = (self.numero_um * self.numero_dois)
        return multiplicacao   
    
    def dividir(self):
        divisao = (self.numero_um / self.numero_dois)
        return divisao   
    
    def elevar(self):
        elevado = (self.numero_um ** self.numero_dois)
        return elevado  
    
    def verificar_numeros(self):
        verificacao = (self.numero_um ^ self.numero_dois)
        return verificacao  
    
    def chamar_numero(self):
        self.numero_um = float(input("Digite primeiro numero: "))
        self.numero_dois = float(input("Digite segundo numero: "))
