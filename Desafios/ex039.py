"""
   Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar no serviço militar
    - se é a hora de se alistar
    - se já passou o tempo do alistamento.

    seu programa também  deverá mostar o tempo que falta ou que passou do prazo. 
"""
import datetime
print('Seja bem vindo ao programa de alistamento')
nascimento = int(input('Em qual ano você nasceu: '))
idade = datetime.date.today().year - nascimento

if (idade < 18):
    print(f'Ainda vai se alistar. Faltam {18 - idade} anos')
elif (idade == 18):
    print(f'Você está com {idade} anos. Está na hora de se alistar')
elif (idade > 18):
    print(f'Já passou o tempo de alistamento. Foi a {idade - 18} anos atrás')
