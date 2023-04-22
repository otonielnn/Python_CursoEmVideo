"""
    Dicionários
    - dicionario['sexo'] = 'M' # adicionando no dicionário.
    - del dicionario['idade'] # remove o elemento.
    - print(dicionario.values()) # printa os valores dos elementos.
    - print(dicionario.keys()) # printa o nome dos elementos.
    - print(dicionario.items()) # printa o elemento e nome.
"""
"""
pessoas = {'nome': 'Otoniel', 'sexo': 'M', 'idade': 21}
pessoas['peso'] = 81.6
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas. items():
    print(f'{k} = {v}')
"""
"""
brasil = list()
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'Rio de Janeiro'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v)
