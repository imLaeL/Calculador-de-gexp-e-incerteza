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
    elif continuar == 'N' or continuar == 'n':
        print('\n\rAté mais, espero que o script tenha sido útil :)')

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
    time.sleep(1)
    repetir = input('\n\rDeseja utilizar outro valor para gexp?(S/N): ')
    
    if repetir == 'S' or repetir == 's':
        calcula_gexp()
    elif repetir == 'N' or repetir == 'n':
        print('\n\rAté mais, espero que o script tenha sido útil :)')

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
    time.sleep(1)
    repetir = input('\n\rDeseja utilizar outro valor para gexp?(S/N): ')
    
    if repetir == 'S' or repetir == 's':
        calcula_incerteza2()
    elif repetir == 'N' or repetir == 'n':
        print('\n\rAté mais, espero que o script tenha sido útil :)')
    


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

try:
    escolha = int(input("O que deseja fazer?(1/2): "))
    
    if escolha == 1:
        try:
            calcula_gexp()
    
        except KeyboardInterrupt:
            print ('\n\rAté mais, espero que o script tenha sido útil :)')

    elif escolha == 2:
        if gexp == 0:
            try:
                calcula_incerteza2()

            except KeyboardInterrupt:
                print('\n\rAté mais, espero que o script tenha sido útil :)')
    
    else:
        try:
            calcula_incerteza()
        
        except KeyboardInterrupt:
            print ('\n\rAté mais, espero que o script tenha sido útil :)')

except KeyboardInterrupt:
    print ('\n\rAté mais, espero que o script tenha sido útil :)')
