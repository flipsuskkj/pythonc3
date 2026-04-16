'''Crie um programa que tenha a função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de calculo do fatorial.'''

def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


print(fatorial(8, show=True))