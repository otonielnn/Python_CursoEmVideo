"""
   Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome. 
"""
print("Seja Bem-vindo ao caça silva")
n = input('Digite seu nome completo: ').strip().lower()
print(f"seu nome tem 'silva': {'silva' in n}")
