'''Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
 aluno individualmente.'''

alunos = []

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    continuar = input("Quer continuar? (S/N): ").upper()
    if continuar == 'N':
        break

# Mostrar boletim
print("\nBOLETIM:")
print(f"{'Nº':<4}{'Nome':<10}{'Média':>8}")
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

# Ver notas individuais
while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para sair): "))

    if opcao == 999:
        print("Encerrando... 📚")
        break

    if opcao < len(alunos):
        print(f"Notas de {alunos[opcao][0]}: {alunos[opcao][1]}")
    else:
        print("Aluno não existe!")