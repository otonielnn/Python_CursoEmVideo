"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

    ao final, mostre o conteudo das três listas.
"""
lista = list()
par = list()
impar = list()
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    q = ''
    while (q != 's' and q != 'n'):
        q = input('Deseja continuar [S/N]? ').strip().lower()
    if (q == 'n'):
        break

for i in lista:
    if (i % 2 == 0):
        par.append(i)
    else:
        impar.append(i)

print('=-' * 30)
print(f'A lista Completa: {lista}')
print(f'Lista com números pares: {par}')
print(f'Lista com números Ímpares: {impar}')
print('=-' * 30)
