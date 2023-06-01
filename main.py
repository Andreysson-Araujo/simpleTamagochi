import os
import random
from random import randrange, randint
from time import sleep


class Tamagochi(object):

    max_fome = 100

    def __init__(self, nome):
        self.nome = nome
        self.fome = randint(20, 60)
        self.diversao = randint(20, 60)

    def contador(self):
        self.fome -= 1
        self.diversao -=5

    def status(self):
        print("=================================")
        print('''
        ░▄▄▄▄░ 
        ▀▀▄██► 
        ▀▀███► 
        ░▀███►░█► 
        ▒▄████▀▀
                ''')
        
        print(f"Alimentação em {self.fome}%")
        print(f"Felicidade em {self.diversao}%")
    
    def comer(self):
        self.diversao -= 10
        print("=================================")
        self.fome += 10
        print('''       
           .-""""-.
          /' .  '. \   
         (`-..:...-')  
          ;-......-;   
           '------'    
 ''')
        print("=================================")
        sleep(1)
        os.system("clear")
        print("=================================")
        print('''       
        
          /' .  '. \   
         (`-..:...-')  
          ;-......-;   
           '------'    
 ''')
        print("=================================")
        sleep(1)
        os.system("clear")
        print("=================================")
        print('''       
        
 
         (`-..:...-')  
          ;-......-;   
           '------'    
 ''')
        print("=================================")
        sleep(1)
        os.system("clear")
        print("=================================")
        print('''       
        
 

          ;-......-;   
           '------'    
 ''')
        print("=================================")
        sleep(1)
        os.system("clear")
        print("=================================")
        print('''
        ░▄▄▄▄░ 
        ▀▀▄██► 
        ▀▀███► 
        ░▀███►░█► 
        ▒▄████▀▀
                ''')
        
        print(f"Alimentação em {self.fome}%")

    def brincar(self):
        itens = ["Pedra", "Papel", "Tesoura"]
        seu_tamagochi = randint(0, 2)
        print("================================\nEscolha:\n[0]Pedra\n[1]Papel\n[2]Tesoura")
        jogada = int(input("Faça sua jogada:"))
        os.system("clear")
        print("==================================")
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        print("==================================")
        os.system("clear")
        print(f"Seu tamagochi jogou {itens[seu_tamagochi]}")
        print(f"Voce jogou {itens[jogada]}")
        self.diversao += 10
        self.fome -= randint(10, 15)

        if jogada == 0 :
            if seu_tamagochi == 0:
                print("Empate")
            elif seu_tamagochi == 1:
                print("Seu tamagochi ganhou")
            elif seu_tamagochi == 2:
                print("Voce Perdeu")
        elif jogada == 1 :
            if seu_tamagochi == 0:
                print("Voce Ganhou")
            elif seu_tamagochi == 1:
                print("Empate")
            elif seu_tamagochi == 2:
                print("Voce Perdeu")
        elif jogada == 2 :
            if seu_tamagochi == 0:
                print("Voce Perdeu")
            elif seu_tamagochi == 1:
                print("Voce Ganhou")
            elif seu_tamagochi == 2:
                print("Empate")
        else:
            print("Jogada invalida")
        print("=================================")
        print('''
        ░▄▄▄▄░ 
        ▀▀▄██► 
        ▀▀███► 
        ░▀███►░█► 
        ▒▄████▀▀
                ''')
        print(f"Felicidade em {self.diversao}%")
        

def main():
    tamagochi_name = input("Qual o nome do seu bichinho?:")

    #Criando tamagochi
    meu_tamagochi = Tamagochi(tamagochi_name)

    input(
        "Ola me chamo " +
        tamagochi_name +
        "\nPressione Enter para continuar."
    )

    escolha = None   


    while escolha != 0:
        print("=================================")
        print("***INTERAJA COM SEU TAMAGOCHI***")
        print("=================================")
        print("[1]- Status")
        print("[2]- Alimentar")
        print("[3]- Brincar")
        print("[0]- Sair")
        print("=================================")
        escolha = int(input("Escolha:"))
        print("=================================")

        if escolha == 1:
            os.system("clear")
            meu_tamagochi.status()
        elif escolha == 2:
            os.system("clear")
            meu_tamagochi.comer()
        elif escolha ==3:
            os.system("clear")
            meu_tamagochi.brincar()
        elif escolha == 0:
            os.system("clear")
            print("Obrigado por jogar")
            break
        else:
            os.system("clear")
            print("Comando invalido")
            


main()