# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
print("Seja Bem-vindo ao sorteador de alunos")
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]
print(f"O escolhido foi {random.choice(lista)}")
