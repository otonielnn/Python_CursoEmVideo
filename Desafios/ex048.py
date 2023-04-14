"""
    Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
print('Todos múltiplos de 3 entre 1 e 500')
s = 0
c = 0
for i in range(0, 501, 3):
    if (i % 2 == 1):
        s += i
        c += 1
print(f'A soma de todos números ímpares, múltiplos de 3 é: {s}')
print(f'O total de números somados foi: {c}')
