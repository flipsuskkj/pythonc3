'''faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia(), e somaPar().
A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior'''


import random
numeros = []
def sorteio():
    for dig in range(0, 5):
        elem = random.randint(1, 50)
        numeros.append(elem)
    print(numeros)
def somaPar():
    count = 0
    for item in numeros:
        if item % 2 == 0:
            count += item
    print(count)

def __main__():
    sorteio()
    somaPar()

__main__()




