class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        
    def emitir_som(self) -> str:
        raise NotImplementedError
    
class Mamifero(Animal):
    def amamentar(self) -> str:
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self) -> str:
        return f"{self.nome} está voando."
    
class Mocergo(Mamifero, Ave):
    def emitir_som(self) -> str:
        return "Mocergo emitem sons ultrassônicos"
    
morcego = Mocergo(nome="Batman")

print("Nome do mocergo:", morcego.nome)
print("Som do mocergo:", morcego.emitir_som())

print("Morcego amametando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())