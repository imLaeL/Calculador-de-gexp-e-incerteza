import math
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

gexp = 0
gref = 9.790863

def calcula_gexp ():

    pi = math.pi
    pi_ao_quadrado = pi * pi

    parte1 = 4 * pi_ao_quadrado

    m = float(input("Digite o valor de m encontrado no gráfico: "))

    parte2 = m * m

    global gexp
    gexp = parte1 / parte2
    gexp_metros = gexp / 100

    time.sleep(1)

    print("\n\rO valor de gexp é: ", gexp)

    print("\n\rPara efetuar a próxima parte do cálculo use o gexp em metros -> ", gexp_metros)
    
    time.sleep(2)

    resposta = input("\n\rVocê deseja utilizar o valor de gexp em metros?(S/N): ")

    if resposta == 'S' or resposta == 's':
        gexp = gexp_metros
        print("\n\rPronto, o valor de gexp agora está em metros!\n")
    
    time.sleep(1)

    continuar = input("Deseja calcular a incerteza agora?(S/N): ")
    
    if continuar == 'S' or continuar == 's':
        calcula_incerteza()

def calcula_incerteza ():
    
    print("\nvalor de gexp que está sendo utilizado-> ", gexp)
    time.sleep(2)
    print("valor de gref que está sendo utilizado -> ", gref)
    time.sleep(2)
    print("Calculando incerteza ...\n")
    time.sleep(0.5)

    parte1 = gexp - gref
    parte2 = parte1 / gexp
    parte3 = parte2 * 100
    print(f'O resultado é de {parte3:,.4f}%')

def calcula_incerteza2 ():
    gexp = float(input("Digite o valor de gexp encontrado: "))
    
    print("\nvalor de gexp que está sendo utilizado-> ", gexp)
    time.sleep(2)
    print("valor de gref que está sendo utilizado -> ", gref)
    time.sleep(2)
    print("Calculando incerteza ...\n")
    time.sleep(0.5)

    parte1 = gexp - gref
    parte2 = parte1 / gexp
    parte3 = parte2 * 100
    print(f'O resultado é de {parte3:,.4f}%')

print('''
   █████████        ████                  ████              █████                 
  ███░░░░░███      ░░███                 ░░███             ░░███                  
 ███     ░░░ ██████ ░███  ██████ █████ ███░███  ██████   ███████  ██████ ████████ 
░███        ░░░░░███░███ ███░░██░░███ ░███░███ ░░░░░███ ███░░███ ███░░██░░███░░███
░███         ███████░███░███ ░░░ ░███ ░███░███  ███████░███ ░███░███ ░███░███ ░░░ 
░░███     █████░░███░███░███  ███░███ ░███░███ ███░░███░███ ░███░███ ░███░███     
 ░░████████░░███████████░░██████ ░░███████████░░███████░░███████░░██████ █████    
  ░░░░░░░░░ ░░░░░░░░░░░░ ░░░░░░   ░░░░░░░░░░░░ ░░░░░░░░ ░░░░░░░░ ░░░░░░ ░░░░░     
     █████                                                                        
    ░░███                                                                         
  ███████  ██████      ███████ ██████ █████ ████████████      ██████              
 ███░░███ ███░░███    ███░░██████░░██░░███ ░░██░░███░░███    ███░░███             
░███ ░███░███████    ░███ ░██░███████ ░░░█████░ ░███ ░███   ░███████              
░███ ░███░███░░░     ░███ ░██░███░░░   ███░░░███░███ ░███   ░███░░░               
░░███████░░██████    ░░██████░░██████ █████ ████░███████    ░░██████              
 ░░░░░░░░ ░░░░░░      ░░░░░███░░░░░░ ░░░░░ ░░░░░░███░░░      ░░░░░░               
                      ███ ░███                  ░███                              
  ███                ░░██████            █████  █████                             
 ░░░                  ░░░░░░            ░░███  ░░░░░                              
 ████████████   ██████  ██████ ████████ ███████   ██████ █████████ ██████         
░░██░░███░░███ ███░░██████░░██░░███░░██░░░███░   ███░░██░█░░░░███ ░░░░░███        
 ░███░███ ░███░███ ░░░░███████ ░███ ░░░  ░███   ░███████░   ███░   ███████        
 ░███░███ ░███░███  ██░███░░░  ░███      ░███ ██░███░░░   ███░   ████░░███        
 ████████ ████░░██████░░██████ █████     ░░█████░░██████ ████████░░████████       
░░░░░░░░ ░░░░░ ░░░░░░  ░░░░░░ ░░░░░       ░░░░░  ░░░░░░ ░░░░░░░░░ ░░░░░░░░        
                                                                                  
                                                                                  
                                                                            
\n
''')

print('''            
            \t\t[1] Calcular gexp
            \t\t[2] Calcular incerteza
''')

escolha = int(input("O que deseja fazer?(1/2): "))

if escolha == 1:
    calcula_gexp()

elif escolha == 2:
    if gexp == 0:
        calcula_incerteza2()
    else:
        calcula_incerteza()

