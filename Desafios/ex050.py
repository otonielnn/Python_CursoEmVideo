"""
    Desenvolva um programa que leia seis números e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar desconsidere-o.
"""
print('Seja Bem-Vindo a soma de pares')
s = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i+1}º número: '))
    if (n % 2 == 0):
        s += n
print(f'A soma de todos números pares digitado foi: {s}')
