"""
    - Fatiamento de string
        nome = otoniel junior
        nome[inicio:final:pulo]
    
    - Analise de string
        len(nome) // retorna o tamanho da string
        nome.count('o') // retorna quantas vezes o parametro aparece na string.
        nome.count('o', 0, 13) // mesma coisa da anterior, com fatiamento. 
        nome.find('nio') // mostra a primeira posição de onde foi encontrado o parametro.
        'Joao' in nome // retornar um boleano (True or False).

    - Transformação
        nome.replace('nio', 'dio') // altera o 1 parametro pelo 2 parametro.
        nome.upper() // deixa em letras maiúsculas.
        nome.lower() // deixa em minúsculas.
        nome.capitalize() // deixa apenas a primeira letra em Maiúsculas.
        nome.title() // deixa em maiúscula toda letra ápos um espaço vazio.
        nome.strip() // retira espaços vázios no começo e final do texto.
        nome.rstrip() // retira espaços vázios da direita.
        nome.lstrip() // retira espaços vázios da esquerda.

    - Divisão
        nome.split() // dividi a string em uma lista

    - Junção
        '-'.join(nome) // retornaria otoniel-junior
"""
frase = "  Curso em Video Python  "
print(frase[1:])
print(frase[:12])
print(frase[1:15])
print(frase[1:12:2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 5))
print(frase.find('deo'))
print(frase.find('urso'))
print('urso' in frase)
print(frase.replace('urso', 'oelho'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print('*'.join(frase))
