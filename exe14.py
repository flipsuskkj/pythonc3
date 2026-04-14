'''crie um programa que crie a matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.'''

matriz = []

for i in range(3):  # 3 linhas
    linha = []
    for j in range(3):  # 3 colunas
        valor = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz:")

for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end="")
    print()