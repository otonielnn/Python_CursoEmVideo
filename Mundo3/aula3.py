"""
teste = list()
teste.append('Otoniel')
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
"""
"""
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
"""
galera = list()
dado = list()
maior = 0
menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é Maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é Menor de idade.')
        menor += 1

print(f'temos {maior} maiores de idade')
print(f'temos {menor} menores de idade')
