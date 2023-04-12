"""
    Faça um programa que leia uma frase pelo teclado e mostre:
        - quantas vezes aparece a letra "A".
        - em que posição ela aparece primeiro.
        - em que posição ela aparece por último.
"""
print('Seja Bem-vindo ao leitor de frases')
frase = input('Digite uma frase: ').strip().lower()
print(f"A frase possui {frase.count('a')} letras 'a' .")
print(f"A primeira letra 'a' aparece na posição {frase.find('a')+1}.")
print(f"A última letra 'a' aparece na posição {frase.rfind('a')+1}.")
