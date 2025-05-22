class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome}, idade={self.idade})"
    
    def saudacao(self) -> str:
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
        
pessoa1: Pessoa = Pessoa("Guilherme Henrique", 26)
saudacao: str = pessoa1.saudacao()

print(pessoa1)
print(saudacao)
print()

pessoa2: Pessoa = Pessoa("Sérgio Henrique", 50)
saudacao = pessoa2.saudacao()

print(pessoa2)
print(saudacao)