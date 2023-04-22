"""
    Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quntas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    q = ''
    while (q != 's' and q != 'n'):
        q = input('Deseja continuar [S/N]? ').lower()[0]
        if (q != 's' and q != 'n'):
            print('ERRO! Responda apenas com S ou N.')
    if (q == 'n'):
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if (busca == 999):
        break
    if (busca >= len(time)):
        print(f'ERRO! Não existe jgoador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'    =>  na partida {i+1}, fez {v} gols.')
# print(f'foi um total de {jogador["total"]} gols.')
