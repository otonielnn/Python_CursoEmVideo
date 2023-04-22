"""
   Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

    Adicione também as docstrings da função. 
"""


def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.

    Args:
        n (float): uma ou mais notas dos alunos (aceita várias).
        sit (bool, optional): Valor opcional, indicando se deve ou não adicionar a situação.

    Returns:
        dict: dicionário com várias informações sobre situação da turma.
    """
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n)/len(n)
    if sit:
        if (notas['media'] > 7):
            notas['situacao'] = 'BOA'
        elif (notas['media'] >= 5):
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'
    return notas


    # Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)
