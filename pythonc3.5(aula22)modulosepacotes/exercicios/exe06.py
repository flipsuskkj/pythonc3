'''Dentro do pacote utilidadesCeV que criamos no desafio 05 temos um módulo chamado dado. crie uma função chamada leiaDinheiro()
 que seja capaz de funcionar com a função input(), mas com uma valiidação de dados para aceitar apenas valores que sejam monetários.
 '''


from utilidadesCeV.moeda import moeda
from utilidadesCeV.dado import dado

preco = dado.leiaDinheiro('Digite o preço: R$')

moeda.resumo(preco, 20, 10)