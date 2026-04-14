'''crie um programa que leia nome, ano de nascimento e cadastre-os (com idade) em um dicionário,
por acaso se a CTPS for diferente de ZERO o dicionário receberá tambem o ano de contratação e o salário.
calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dados = {}

dados['nome'] = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - ano_nascimento

ctps = int(input("CTPS (0 não tem): "))
dados['ctps'] = ctps

if ctps != 0:
    ano_contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))
    dados['ano_contratacao'] = ano_contratacao
    dados['salario'] = salario
    dados['aposentadoria'] = dados['idade'] + ((ano_contratacao + 35) - datetime.now().year)

for chave, valor in dados.items():
    print(f"{chave}: {valor}")