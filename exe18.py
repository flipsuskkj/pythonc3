'''faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário.
No final, mostre o conteudo da estrutura na tela.'''

aluno = {}

aluno['nome'] = input("Nome do aluno: ")
aluno['media'] = float(input("Média do aluno: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print("\n--- Resultado ---")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")