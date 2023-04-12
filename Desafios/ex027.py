"""
    Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
    ex: Otoniel carvalho de mendonça junior
    primeiro = otoniel
    ultimo = junior
"""
print('Seja bem-vindo ao programa que mostra seu primeiro e último nome')
n = input('Digite seu nome completo: ').strip().lower()
nomes = n.split()
print(f'seu primeiro nome é {nomes[0]}')
print(f'seu último nome é {nomes[-1]}')
