# PROJETO 2 - CHUTE UM NUMERO DE 1 A 10
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o
usuário chute um número até que o valor gerado no inicio do programa seja chutado corretamente.

O programa deverá informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado
no inicio do programa.
'''

import random
valor_aleatório = random.randint(1,10)
acertou = False
while acertou == False:
    valor_usuario = int(input('Escolha um Valor de 1 a 10: '))
    if valor_usuario == valor_aleatório:
        acertou = True
        print('Parabéns, você acertou o chute')
    elif valor_usuario > valor_aleatório:
        print('Chute mais baixo')
    elif valor_usuario < valor_aleatório:
        print('Chute mais alto')
