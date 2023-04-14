"""
   Crie Um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média antigida:
    - Média abaixo de 5: Reprovado
    - Média entre 5 e 6.9: Recuperação
    - Média 7 ou superior: Aprovado 
"""
print('Seja bem-vindo ao calculador de média')
n1 = float(input('Digite sua 1º nota: '))
n2 = float(input('Digite sua 2º nota: '))
media = (n1 + n2) / 2

print(f'Com notas {n1:.1f} e {n2:.1f}, a média ficou {media:.1f}')

if (media >= 7):
    print('Você está aprovado')
elif (media > 5 and media <= 6.9):
    print('Você está em Recuperação')
elif (media < 5):
    print('Você está Reprovado')
