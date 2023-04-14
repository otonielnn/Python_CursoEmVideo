"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final. mostre:
        - quantas pessoas tem mais de 18anos.
        - quantos homens foram cadastrados.
        - quantas mulheres tem menos de 20anos.
"""
tot18 = 0
m20 = 0
homem = 0
while (True):
    idade = int(input('idade: '))
    sexo = ''
    resp = ''
    while (sexo != 'm' and sexo != 'f'):
        sexo = input('sexo [M/F]: ').strip().lower()[0]
    if (idade >= 18):
        tot18 += 1
    if (sexo == 'm'):
        homem += 1
    if (sexo == 'f' and idade < 20):
        m20 += 1
    while (resp != 's' and resp != 'n'):
        resp = input('Quer continuar [S/N]? ').strip().lower()[0]
    if (resp == 'n'):
        break


print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {m20}')
