# PROJETO 1 - FATORIAL
'''
Crie um programa que receba um número e imprima o fatorial daquele número
# Devemos usar os 5 Qs:
1 - Quais são os dados de entrada necessários?
2 - O que eu devo fazer com esses dados?
3 - Quais são as restrições deste problema?
4 - Qual o resultado esperado?
5 - Qual a sequência de passos a serem feitas para chegar ao resultado esperado?
'''

numero_solicitado = int(input('Informe um numero '))
if numero_solicitado > 0:
    fatorial = 1
    for item in range(1,numero_solicitado +1):
        fatorial = fatorial * item
    print(fatorial)
