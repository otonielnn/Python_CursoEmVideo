"""
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random
vitorias = 0
while (True):
    nJogador = int(input('Digite um valor: '))
    ipJogador = input('Par ou Ímpar [P/I]: ').strip().lower()[0]
    nComputador = random.randint(0, 20)
    soma = nJogador + nComputador
    resultado = soma % 2

    while (ipJogador != 'p' and ipJogador != 'i'):
        ipJogador = input('Par ou Ímpar [P/I]: ').strip().lower()[0]
    print(
        f'Você jogou {nJogador} e o computador {nComputador}. Total de {soma} ', end='')

    if (resultado == 0):
        print('Deu PAR')
    else:
        print('Deu Ìmpar')

    if (ipJogador == 'p'):
        if (resultado == 0):
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU')
            break
    elif (ipJogador == 'i'):
        if (resultado == 1):
            print('Você VENCEU')
            vitorias += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {vitorias} partidas consecutivas.')
