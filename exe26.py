'''Faça um programa que tenha uma função chamada contador().
Que receba três parâmetros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) de 1 até 10 de 1 em 1
B) de 10 até 0 de 2 em 2
C) Uma contagem personalizada'''


def caso1(inicio, fim, passo):
    for c in range(inicio, fim - 1, -passo):
        if c == fim:
            print(f'{c}', end='')
        else:
            print(f'{c} - ', end='')


def caso2(inicio, fim, passo):
    for c in range(inicio, fim - 1, passo):
        if c == fim:
            print(f'{c}', end='')
        else:
            print(f'{c} - ', end='')


def caso3(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        if c == fim:
            print(f'{c}', end='')
        else:
            print(f'{c} - ', end='')


def contador():
    print('De 1 até 10: ')
    for c in range(0, 10):
        if c == 9:
            print(f'{c + 1}', end='')
        else:
            print(f'{c + 1} - ', end='')
    print('\n\nDe 10 até 0: ')
    for c in range(10, -1, -2):
        if c == 0:
            print(f'{c}\n')
        else:
            print(f'{c} - ', end='')
    inicio = int(input('Insira o primeiro elemento: '))
    fim = int(input('Insira o último elemento: '))
    passo = int(input('Insira o passo: '))

    if passo == 0:
        passo = 1
    if inicio > fim:
        caso1(inicio, fim, passo)
    if passo < 0:
        caso2(inicio, fim, passo)
    if inicio < fim:
        caso3(inicio, fim, passo)

contador()