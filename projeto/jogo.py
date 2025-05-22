import  random

class Personagem:
    def __init__(self, nome: str, vida: int, nivel: int):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhe(self):
        return (f"Nome: {self.get_nome()}\n"
                f"Vida: {self.get_vida()}\n"
                f"Nível: {self.get_nivel()}")
    
    def receber_ataque(self, dano: int):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo: "Personagem"):
        dano: int = random.randint(self.__nivel * 2, self.__nivel * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        
    
class Heroi(Personagem):
    def __init__(self, nome: str, vida: int, nivel: int, habilidade: str):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo: Personagem):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} com ataque especial e causou {dano} de dano!")

    
class Inimigo(Personagem):
    def __init__(self, nome: str, vida: int, nivel: int, tipo: str):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nTipo: {self.get_tipo()}"
    
    
class Jogo:
    """Classe orquestradora do jogo"""
    
    def __init__(self):
        self.heroi: Heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")
        
    def iniciar_batalha(self):
        """Fazer a gestão de batalha em turnos"""
        print("Iniciando batalha!")
        
        while(self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0):
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhe())
            print("\n" + self.inimigo.exibir_detalhe())
            
            input("\nPressione Enter para atacar...")
            escolha: str = input("Escolha (1 - Ataque normal, 2 - Ataque especial): ")
            escolha_valida: bool = True
            
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                escolha_valida = False
                print("Escolha inválida. Tente novamente.")
                
            if escolha_valida and self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
                
        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")
            
jogo: Jogo = Jogo()
jogo.iniciar_batalha()