import os

def mostrar_linha(a, b, c):
    print ([a, b, c])

def multiplicacao(x, y, z):
    x * y * z

det_matriz = True

while det_matriz:
    (mostrar_linha('A', 'B', 'C'), '\r\n')
    (mostrar_linha('D', 'E', 'F'), '\r\n')
    (mostrar_linha('G', 'H', 'I'), '\r\n')

    
    try:
        numero_A = float(input('Digite um número para o valor "A": '))
        numero_B = float(input('Digite um número para o valor "B": '))
        numero_C = float(input('Digite um número para o valor "C": '))
        numero_D = float(input('Digite um número para o valor "D": '))
        numero_E = float(input('Digite um número para o valor "E": '))
        numero_F = float(input('Digite um número para o valor "F": '))
        numero_G = float(input('Digite um número para o valor "G": '))
        numero_H = float(input('Digite um número para o valor "H": '))
        numero_I = float(input('Digite um número para o valor "I": '))
    except:
        os.system('cls')
        print(10*'-')
        print('Erro. Tente novamente.')
        print(10*'-')
        continue

    print('Sua matriz é:')
    mostrar_linha(numero_A, numero_B, numero_C)
    mostrar_linha(numero_D, numero_E, numero_F)
    mostrar_linha(numero_G, numero_H, numero_I)

    aei = numero_A * numero_E * numero_I
    bfg = numero_B * numero_F * numero_G
    cdh = numero_C * numero_D * numero_H

    ceg = numero_C * numero_E * numero_G
    afh = numero_A * numero_F * numero_H
    bdi = numero_B * numero_D * numero_I

    sarrusA = aei + bfg + cdh
    sarrusB = ceg + afh + bdi
    print('A determinante desta matriz é:')
    print(f'DET = {sarrusA - sarrusB}')

    print('Deseja calcular a determinante de outra matriz?')
    continuar = input('[s]im [n]ão: ').lower()
    print(10*'-')
    if continuar == 's':
        det_matriz = True
    else:
        print('Até a próxima :D')
        break
