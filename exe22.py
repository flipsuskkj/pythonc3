'''crie um programa que leia nome, idade e sexo de várias pessoas,
guardando os dados de cada uma pessoa em dicionário e todos os dicionários em uma lista.
no final mostre:

A) quantas pessoas foram cadastradas
B) A média da idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.'''

pessoas = []
sid = 0

while True:
    pessoa = {}

    pessoa['nome'] = input("Nome: ")
    pessoa['idade'] = int(input("Idade: "))
    pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()

    pessoas.append(pessoa)
    sid += pessoa['idade']

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

media = sid / len(pessoas)

print(f"\nA) Total de pessoas: {len(pessoas)}")
print(f"B) Média de idade: {media:.2f}")

print("C) Mulheres:")
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'])

print("D) Pessoas com idade acima da média:")
for p in pessoas:
    if p['idade'] > media:
        print(f"{p['nome']} ({p['idade']})")