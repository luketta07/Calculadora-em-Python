import time
import random
class perso:
    #atributos
    def __init__(self, nome, vida, forca, defesa, nomepoder, danopoder):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.nomepoder = nomepoder
        self.danopoder = danopoder
    
    def sofrer_dano(self, quantidade):
         danoreal = quantidade - self.defesa
         self.vida -= danoreal
         if self.vida<=0:
             self.vida=0
             print ("{} sofreu {} de dano.\nPorém {} tem {} de defesa.\n{} sofreu entao {} de dano\nA vida restante de {} é {}\n".format(self.nome, quantidade, self.nome, self.defesa,self.nome, danoreal, self.nome, self.vida))
             
    def atacar (self, alvo):
        print("{} atacou {} com forca {}".format(self.nome, alvo.nome, self.forca, ))
        alvo.sofrer_dano(self.forca)
        
    def ataquepoder (self, alvo):
        alvo.vida -= self.danopoder
        if alvo.vida<=0:
            alvo.vida=0
        print("{} soltou o {}, e deu {} de dano\n{} recebeu um ataque especial, que furou totalmente sua defesa.\n{} sofreu entao {} de dano\nA vida restante de {} é {}\n".format(self.nome, self.nomepoder, self.danopoder, alvo.nome, alvo.nome, self.danopoder, alvo.nome, alvo.vida ))
 
def escolha():
    if heroi.vida <= 0:
        encerrav()
        
        
    primeiraescolha = input("Seu personagem Monkey D. luffy\ndigite:\n1 para atacar\n2 para ataque especial\n3 para desistir da batalha\nO que voce vai escolher fazer?\n")
    if primeiraescolha == "1":
        heroi.atacar(vilao)
        vilaoesc()
    elif primeiraescolha == "2":
        heroi.ataquepoder(vilao)
        vilaoesc()
    elif primeiraescolha =="3":
        print("Você perdeu a batalha\n Luffy foi morto, todos o Mugiwaras perderam a fé, e viraram escravos do Kaidou.")
        encerrav()
    else:
        print('Coloque uma resposta válida')
        escolha()
        
def vilaoesc():
    if vilao.vida <=0:
        print("voce venceu")
        encerrah()
    danorandom=random.randint(1,3)
    if danorandom == 1:
        vilao.atacar(heroi)
        escolha()
    elif danorandom==2:
        vilao.ataquepoder(heroi)
        escolha()
    elif danorandom==3:
        print("Kaidou errou seu ataque, nao surgiu efeito nenhum em luffy")
        escolha()
        
def encerrah():
    print("Luffy amaasou a cara do kaidou, e esta ainda mais próximo de se tornar o rei dos piratas.\n")
    time.sleep(2)
    print("fim da batalha")
    comeco2()
def encerrav():
    volta=input('você perdeu...\n1 se deseja voltar a tela de inicio\n2 caso queira tentar novamente')
    if volta=="1":
        comeco()
    elif volta=="2":
        reiniciar()
            
def reiniciar():
    print("Luffy vs Kaidou")
    time.sleep(2)
    print("Fight")
    time.sleep(1)
    print("Luffy:\n-EU VOU ME TORNAR O REI DOS PIRATAS!\nKaidou:\n-Todos que me desafiarem, enfrentaram minha fúria, OU, RO, RO, RO, RO, RO.\n ")
    time.sleep(2)
    escolha()
    
def comeco():    
    começo = input("Deseja fazer uma batalha teste?(s ou n)\n")
    if começo=="s":
        print("Luffy vs Kaidou")
        time.sleep(2)
        print("Fight")
        time.sleep(1)
        print("Luffy:\n-EU VOU ME TORNAR O REI DOS PIRATAS!\nKaidou:\n-Todos que me desafiarem, enfrentaram  minha fúria, OU, RO, RO, RO, RO, RO.\n ")
        time.sleep(2)
        escolha()
    elif começo=="n":
        print("Ok, até a próxima")
    else:
        print("coloque uma resposta valida")
        comeco()

def comeco2():    
    começo = input("Deseja fazer uma outra batalha teste?(s ou n)\n")
    if começo=="s":
        print("Luffy vs Kaidou")
        time.sleep(2)
        print("Fight")
        time.sleep(1)
        print("Luffy:\n-EU VOU ME TORNAR O REI DOS PIRATAS!\nKaidou:\n-Todos que me desafiarem, enfrentaram  minha fúria, OU, RO, RO, RO, RO, RO.\n ")
        time.sleep(2)
        escolha()
    elif começo=="n":
        print("Ok, até a próxima")
    else:
        print("coloque uma resposta valida")
        comeco()


heroi = perso( "Luffy",500, 100, 50,"Gomu Gomu no Elephant Gatling", 200)
vilao = perso("Kaidou", 500, 100, 50, "Boro Breath", 400)

print("Seja bem-vindo ao battle animes\n")
time.sleep(1)

comeco()
