'''faça um programa que tenha a função ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'

    if gols == '':
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s).')

n = input('Nome do jogador: ')
g = input('Número de gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0

ficha(n, g)