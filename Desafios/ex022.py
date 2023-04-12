"""
    Crie um programa que leia o nome completo de uma pessoa e mostre
        - O nome com todas letras maiúsculas.
        - O nome com todas letras minúsculas.
        - quantas letras ao todo (sem considerar espaços).
        - quantas letras tem o primeiro nome.
"""
print("Seja bem-vindo a analise de nome")
nome = input("Digite seu nome completo: ").strip()
print(f"seu nome em Maiúsculas: {nome.upper()}")
print(f"seu nome em Minúsculas: {nome.lower()}")
print(f"total de letras que seu nome tem: {len(nome)-nome.count(' ')}")
nomes = nome.split()
print(f"Seu primeiro nome é {nomes[0]} e ele tem: {nome.find(' ')}")
