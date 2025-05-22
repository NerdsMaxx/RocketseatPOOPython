class MinhaClasse:
    valor = 10 #Atributo da classe (como se fosse static do Java)

    def __init__(self, nome: str):
        self.nome = nome #Atributo da instância

    def metodo_instancia(self):
        return f"Método de instância para {self.nome} e {self.valor}"

    @classmethod
    def metodo_classe(cls): #parecido com método static, mas diferente
        return f"Método de classe chamado para valor = {cls.valor}"

    # parecido com método static, mas não recebe nenhum argumentos,
    # não acessa os atributos da classe
    @staticmethod
    def metodo_estatico():
        return f"Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return f"Carro[marca={self.marca},modelo={self.modelo},ano={self.ano}]"

    @classmethod
    def criar_carro(cls, configuracao: str):
        marca, modelo, ano = configuracao.split(",")
        return Carro(marca=marca, modelo=modelo, ano=int(ano))
    
configuracao: str = "Toyota,Corolla,2022"
carro: Carro = Carro.criar_carro(configuracao)
print(carro)

class Matematica:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
print(Matematica.somar(5,9))