"""
    Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre
        - Apenas 5 primeiros colocados
        - Os últimos colocados da tabela
        - Uma lista com os times em ordem alfabetica.
        - Em que posição na taela está o time da chapecoense.
"""
times = ('Corithians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlétio-PR', 'Bahia',
         'São paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
q = len(times)

print('=-'*20)

for i in range(0, 5):
    print(f'{i+1} - {times[i]}')

print('=-'*20)

for i in range(-1, -6, -1):
    print(f'{q} - {times[i]}')
    q -= 1

print('=-'*20)
print(sorted(times))
print('=-'*20)
chapecoense = times.index('Chapecoense') + 1
print(f'{chapecoense} - {times[7]}')
