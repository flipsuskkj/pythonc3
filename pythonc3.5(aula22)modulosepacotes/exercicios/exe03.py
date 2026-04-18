'''modifique as funções que foram criadas no desafio 01 para que elas aceitem
 um parâmetro a mais, informando se o valor retornado por elas vai ser ou não vai
 ser formatado pela função moeda(), desenvolvida no exercício 02'''

import moeda3

preco = 200

print(moeda3.aumentar(preco, 10))          # 220.0
print(moeda3.aumentar(preco, 10, True))    # R$220,00

print(moeda3.metade(preco, True))          # R$100,00
print(moeda3.dobro(preco))                 # 400