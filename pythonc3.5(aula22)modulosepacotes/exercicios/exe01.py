'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()'''

import moeda

preco = 100

print(moeda.aumentar(preco, 10, True))  # R$110,00
print(moeda.diminuir(preco, 20, True))  # R$80,00
print(moeda.dobro(preco, True))         # R$200,00
print(moeda.metade(preco, True))        # R$50,00