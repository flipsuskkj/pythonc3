'''crie um programa que vai gerar cinco numeros aleatorios e colocar numa tupla.

Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maio valor que estão na tupla.'''
from random import randint as rd

a = (rd(1,10), rd(1,10), rd(1,10), rd(1,10), rd(1,10))

print(a)
print(sorted(a))
print(min(a))
print(max(a))
