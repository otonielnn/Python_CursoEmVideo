"""
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, Você deve mostrar, para cada palavra, quais são as suas vogais.
"""
tupla = ('otoniel', 'carvalho', 'de', 'Mendonca', 'junior')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in tupla:
    print(f'A palavra é: {p}')
    for letra in p:
        if letra.lower() in vogais:
            print(letra)
