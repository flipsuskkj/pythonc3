'''faça uma função que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a area do terreno.'''
from time import sleep as slp
def ter(lar, comp):
    slp(1)
    print('-' * 30)
    lar = int(input('Digite um valor para a largura (m): '))
    print('-' * 30)
    slp(1)
    print('-' * 30)
    comp = int(input('Digite um valor para a comprimento (m): '))
    print('-' * 30)
    terr = lar*comp
    slp(1)
    print('-' * 30)
    print(f'Seu terreno de {lar}m de largura e {comp}m de comprimento tem {terr}m² ')
    print('-' * 30)

ter(0,0)

