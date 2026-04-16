'''crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional
ou obrigatório nas eleições. '''

def voto(anonas):
    if 2026 - anonas < 16:
        return 'NEGADO'
    elif 2026 - anonas == 16 or 2026 - anonas == 17:
        return 'OPCIONAL'
    elif 2026 - anonas >= 18:
        return 'OBRIGATÓRIO'


anonas = int(input('Em que ano você nasceu? '))
print(f'Você nasceu em {anonas} tem {2026 - anonas} anos de idade e o seu voto é {voto(anonas)}')
    