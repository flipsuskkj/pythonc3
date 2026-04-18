'''adapte o código do desafio 1 dessa aula, crisando uma função adcional chamada moeda()
 que consiga mostrar os valores como um valor monetário formatado'''

import moeda2

preco = 150

aumento = moeda2.aumentar(preco, 10)
print(moeda2.moeda(aumento))  # R$165,00

print(moeda2.moeda(moeda2.dobro(preco)))   # R$300,00
print(moeda2.moeda(moeda2.metade(preco)))  # R$75,00