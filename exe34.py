'''Faça um mini-sistema que utilize do interactive help do python. o ususario vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra 'FIM',
o programa se encerrará. obs: use cores.

'''


def cor(texto, cor=0):
    cores = {
        0: '\033[m',  # reset
        1: '\033[31m',  # vermelho
        2: '\033[32m',  # verde
        3: '\033[33m',  # amarelo
        4: '\033[34m',  # azul
        5: '\033[35m',  # roxo
        6: '\033[36m'  # ciano
    }
    return f"{cores.get(cor, '\033[m')}{texto}\033[m"


def titulo(msg):
    print(cor('=' * 40, 3))
    print(cor(msg.center(40), 5))
    print(cor('=' * 40, 3))


while True:
    titulo('SISTEMA DE AJUDA PYTHON')

    comando = input(cor('Função ou Biblioteca > ', 6))

    if comando.strip().upper() == 'FIM':
        titulo('ATÉ LOGO!')
        break

    titulo(f'Acessando manual de "{comando}"')
    print(cor('', 0))

    help(comando)