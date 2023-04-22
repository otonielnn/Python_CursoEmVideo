"""
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando uma valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATORIO nas eleições.
"""


def voto():
    from datetime import datetime
    print('-' * 20)
    nasc = int(input('Em que ano você nasceu? '))
    ano = datetime.today().year
    idade = ano - nasc
    if (idade < 16):
        print(f'Com {idade} anos: NÃO VOTA.')
    elif (16 <= idade < 18):
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATORIO')


voto()
