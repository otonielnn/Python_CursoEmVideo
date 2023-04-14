"""
    Desenvolva um programa que leia um primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dssa progressão
"""
print("Os 10 Termos iniciais de PA")
ti = int(input('Digite o Termo Inicial: '))
r = int(input('Digite a Razão: '))
decimo = ti + (10 - 1) * r
for i in range(ti, decimo+r, r):
    print(i, end=' ')
