'''Aprimore o programa anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A Soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = []

soma_pares = 0
soma_terceira_coluna = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(valor)

        # A) soma dos pares
        if valor % 2 == 0:
            soma_pares += valor

        # B) soma da terceira coluna (coluna 2)
        if j == 2:
            soma_terceira_coluna += valor

    matriz.append(linha)

# C) maior valor da segunda linha (linha 1)
maior_segunda_linha = max(matriz[1])

# Mostrar matriz
print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end="")
    print()

# Resultados
print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")