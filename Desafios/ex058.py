"""
    Melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random
print('Jogo da Adivinhação v2.0')
tentativa = int()
numero = (random.randint(0, 10))
palpites = 1

while (tentativa != numero):
    tentativa = int(input('Digite um número entre 0 e 10: '))
    if (tentativa == numero):
        print(f'Parabéns, eu estava pensando no número: {numero}')
    elif (tentativa < numero):
        print('Mais... Tente novamente')
        palpites += 1
    elif (tentativa > numero):
        print('Menos... tente novamente')
        palpites += 1
print(f'Você deu {palpites} palpites')
