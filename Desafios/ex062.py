"""
    Melhore o desafio 061, perguntando  para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('Progressão Aritmética v3.0')
primeiro = int(input('Digite o Termo Inicial: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while (mais != 0):
    total += mais
    while (cont <= total):
        print(f'{termo}', end=' - ')
        termo += razao
        cont += 1
    print('pause')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados')
