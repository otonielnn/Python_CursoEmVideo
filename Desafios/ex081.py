"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    depois disso, mostre:
        - Quantos números foram digitados.
        - A lista de valores ordenada de forma decrescente.
        - se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()
while True:
    n = int(input('Digite um número: '))
    q = ''
    lista.append(n)
    while (q != 's' and q != 'n'):
        q = input('Deseja continuar [S/N]? ').strip().lower()
    if (q == 'n'):
        break

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if (5 in lista):
    print('O número 5 está na lista.')
else:
    print('O número 5 não foi digitado.')
