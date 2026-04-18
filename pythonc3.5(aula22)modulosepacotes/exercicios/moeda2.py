def aumentar(valor, percentual):
    return valor + (valor * percentual / 100)


def diminuir(valor, percentual):
    return valor - (valor * percentual / 100)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')