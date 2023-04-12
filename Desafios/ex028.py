"""
    Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador (O programa deverá escrever se o usuário venceu ou perdeu)
"""
import random
print('Tente advinhar em qual número eu estou pensando entre 0 e 5: ')
tentativa = int(input('Digite um número de 0 a 5: '))
numero = (random.randint(0, 5))
if (tentativa == numero):
    print(f"Parabéns, eu estava pensando no número {numero}")
else:
    print(f"Não foi dessa vez... eu estava pensando no número {numero}")
