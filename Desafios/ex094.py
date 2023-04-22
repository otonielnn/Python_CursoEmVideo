"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
        - quantas pessoas foram cadastradas.
        - a média de idade do grupo.
        - uma lista com todas as mulheres.
        - uma lista com todas as pessoas com idade acima da média.
"""
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if (pessoa['sexo'] in 'MF'):
            break
        print('ERRo! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    q = ''
    while (q != 's' and q != 'n'):
        q = input('Quer continuar [S/N]? ').lower()[0]
        if (q != 's' and q != 'n'):
            print('ERRO! Responda apenas com S ou N.')
    if (q == 'n'):
        break
print('-=' * 30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade do grupo é de {media:.0f} anos.')
print('C) As mulheres cadastradas foram:', end='')
for p in galera:
    if (p['sexo'] == 'F'):
        print(f' {p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da idade média:', end='')
for p in galera:
    if (p['idade'] >= media):
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
