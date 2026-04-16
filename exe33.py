'''Faça um programa que tenha uma função chamada notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas;
- a maior nota
- a menor nota
- a media da turma
- a situação (opcional) 

adcione as docstrings da função tambem'''

def notas(*n, sit=False):
    """
    Função para analisar notas e gerar um resumo da turma.

    Parâmetros:
    *n (float): uma ou mais notas dos alunos
    sit (bool, opcional): indica se deve mostrar a situação da turma

    Retorna:
    dict: dicionário com quantidade de notas, maior, menor, média e situação (opcional)
    """

    dados = {}

    # quantidade de notas
    dados['total'] = len(n)

    # maior e menor nota
    dados['maior'] = max(n)
    dados['menor'] = min(n)

    # média
    dados['media'] = sum(n) / len(n)

    # situação (opcional)
    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOÁVEL'
        else:
            dados['situacao'] = 'RUIM'

    return dados