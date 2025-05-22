# Exemplo de herança
from typing import Any

print("\nExemplo de herança:")


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    def emitir_som(self) -> Any:
        pass


class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "Au, au"


class Gato(Animal):
    def emitir_som(self) -> str:
        return "Miau!"


cachorro: Cachorro = Cachorro(nome="Chico")
gato: Gato = Gato(nome="Lua")

print("\nExemplo de polimorfismo")
animais: list[Animal] = [cachorro, gato]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")


class ContaBancaria:
    def __init__(self, saldo: float) -> None:
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor: float):
        if valor > 0.00:
            self.__saldo += valor

    def sacar(self, valor: float):
        if valor > 0.00 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self) -> float:
        return self.__saldo


conta: ContaBancaria = ContaBancaria(saldo=1000.00)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(valor=500.00)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(valor=-500.00)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(valor=2000.00)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(valor=200.00)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self) -> str:
        pass
    
    @abstractmethod
    def desligar(self) -> str:
        pass
    
class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self) -> str:
        return "Carro ligado"

    def desligar(self) -> str:
        return "Carro desligado"
    
carro: Carro = Carro()
print(carro.ligar())
print(carro.desligar())