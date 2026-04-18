'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()'''

def aumentar(valor, percentual, formatar=False):
    resultado = valor + (valor * percentual / 100)
    return resultado if not formatar else moeda(resultado)


def diminuir(valor, percentual, formatar=False):
    resultado = valor - (valor * percentual / 100)
    return resultado if not formatar else moeda(resultado)


def dobro(valor, formatar=False):
    resultado = valor * 2
    return resultado if not formatar else moeda(resultado)


def metade(valor, formatar=False):
    resultado = valor / 2
    return resultado if not formatar else moeda(resultado)


def moeda(valor, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')