import time

def escolha():
    escolha=input("Voce deseja calcular(sim ou nao)? ")
    if escolha=="sim":
        escolha1()
    elif escolha=="nao":
        print("Ok, até a proxima")
    else:
        print("por favor,  escolha uma resposta válida")
        escolha()

def escolha1():
    sinal=input("escolha qual sinal voce quer calcular menos(-), mais(+), multiplicação(*), divisão(/) ou porcentagem(%): ")
    if sinal=="-":
        subtracao()
   
    elif sinal=="+":
        adicao()
   
    elif sinal=="*":
        multiplica()
   
    elif sinal=="/":
        divisao()
   
    elif sinal=="%":
        porcentagem()
   
    else:
        print("escolha um dos simbolos que simbolizam os sinais, se voce nao quer calcular vai se lascar")
        escolha1()

def subtracao():
    n1=float(input("Escolha o primeiro numero (ele precisa ser quebrado): "))
    time.sleep(1)
    n2=float(input("Agora escolha o segundo numero para fazer o calculo: "))
    resultadosub=(n1-n2)
    print(n1 ,"-",n2 ,"=",resultadosub ,)
    time.sleep(4)
    denovo=input("deseja calcular novamente (sim ou não) ? ")
    if denovo=="sim":
        escolha1()
    elif denovo=="nao":
        print("muito obrigado ate a proxima")
    else:
        print('vai se lascar')

def adicao():
    n1=float(input("Escolha o primeiro numero (ele precisa ser quebrado): "))
    time.sleep(1)
    n2=float(input("Agora escolha o segundo numero para fazer o calculo: "))
    resultadoadi=(n1+n2)
    print(n1 ,"+",n2 ,"=",resultadoadi , )
    time.sleep(4)
    denovo=input("deseja calcular novamente (sim ou não) ? ")
    if denovo=="sim":
        escolha1()
    elif denovo=="nao":
        print("muito obrigado ate a proxima")
    else:
        print('vai se lascar')
   
def multiplica():
    n1=float(input("Escolha o primeiro numero (ele precisa ser quebrado):  "))
    time.sleep(1)
    n2=float(input("Agora escolha o segundo numero para fazer o calculo: "))
    resultadomul=(n1*n2)
    print(n1 ,"x",n2 ,"=",resultadomul , )
    time.sleep(4)
    denovo=input("deseja calcular novamente (sim ou não) ? ")
    if denovo=="sim":
        escolha1()
    elif denovo=="nao":
        print("muito obrigado ate a proxima")
    else:
        print('vai se lascar')

def divisao():
    n1=float(input("Escolha o primeiro numero (ele precisa ser quebrado): "))
    time.sleep(1)
    n2=float(input("Agora escolha o segundo numero para fazer o calculo: "))
    resultadodiv=(n1/n2)
    print(n1 ,":",n2 ,"=",resultadodiv , )
    time.sleep(4)
    denovo=input("deseja calcular novamente (sim ou não) ? ")
    if denovo=="sim":
        escolha1()
    elif denovo=="nao":
        print("muito obrigado ate a proxima")
    else:
        print('vai se lascar')
       
def porcentagem():
    n1=float(input("escolha o numero que voce deseja saber a porcentagem: "))
    time.sleep(1)
    n2=int(input("digite a porcentagem que voce deseja saber do seu numero escolhido"))
   
    resultporcem=(n1*n2/100)
    print(resultporcem)
    time.sleep(4)
    denovo=input("deseja calcular novamente (sim ou não) ? ")
    if denovo=="sim":
        escolha1()
    elif denovo=="nao":
        print("muito obrigado ate a proxima")
    else:
        print('vai se lascar')

print ("Olá")
time.sleep(2)
escolha()
