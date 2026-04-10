'''crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos valores
na sequencia.
No final, mostre uma listagem de preços organizando os dados em forma tabular(?)'''

produtos = (
    "Lápis", 1.50,
    "Caderno", 15.90,
    "Borracha", 2.00,
    "Mochila", 120.00,
    "Caneta", 3.50,
    "Livro", 45.00
)

print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:.<30} R$ {preco:>6.2f}")

print("-" * 40)