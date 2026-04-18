'''crie um pacote chamadio utilidadesCeV que tenha dois módulos internos chamdados moeda e dado.

Transfira todas as funções utilizadas nos desafios 01,02 e 03 para o primeiro pacote e mantenha tudo funcionando.'''

from utilidadesCeV.moeda import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 10)