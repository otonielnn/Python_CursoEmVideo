"""
   A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com idade:
    - Até 9 anos: Mirim
    - Até 14 anos: Infantil 
    - Até 19 anos: junior
    - Até 25 anos: Senior 
    - Acima : Master 
"""
import datetime
print('Bem vindo ao programa da Confederação Nacional de Natação')
nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nascimento

print(f'O atleta tem {idade} anos.')
if (idade <= 9):
    print('Você está na categoria Mirim')
elif (idade > 9 and idade <= 14):
    print('Você está na categoria Infántil')
elif (idade > 14 and idade <= 19):
    print('Você está na categoria Júnior')
elif (idade > 19 and idade <= 25):
    print('Você está na categoria Senior')
elif (idade > 25):
    print('Você está na categoria master')
