from typing import Callable, Any

def meu_decorar(func: Callable[[], Any]):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")

    return wrapper

@meu_decorar
def minha_funcao():
    print("Minha função foi chamada")
    
minha_funcao()

class MeuDecoradorDeClasses:
    def __init__(self, func: Callable):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print("Antes da função ser chamada (decorador de classes)")
        self.func()
        print("Depois da função ser chamada (decorador de classes)")

@MeuDecoradorDeClasses
def segunda_funcao():
    print("Segunda função foi chamada")

print()
segunda_funcao()
    
