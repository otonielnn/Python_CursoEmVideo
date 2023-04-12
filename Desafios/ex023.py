"""
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
    
    EX: 1834
    unidade 4
    dezena 3
    centena 8
    milhar 1
"""
print("Seja Bem-vindo ao separador de digitos")
n = str(input('Digite um número de 0 a 9999: '))
n.split()
unidade = print(f'Unidade {n[3]}')
dezena = print(f'Dezena {n[2]}')
centena = print(f'Centena {n[1]}')
milhar = print(f'Milhar {n[0]}')
