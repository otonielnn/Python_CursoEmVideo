"""
   Crie um programa que leia o nome da cidade e diga se ela começa ou não com o nome "SANTO". 
"""
print('Verificador de nome de cidade')
cidade = input('Digite o nome de sua cidade: ').strip().lower()
print(cidade[:5] == 'santo')
