"""
    Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
print("Bem-vindo ao programa de tabuada.")
n = int(input("Digite o número que você deseja ver a tabuada: "))
for i in range(0, 11):
    print(f"{n} x {i} = {n * i}")
