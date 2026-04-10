'''Crie um programa que tenha uma tupla preenchida com uma contagem por extenso, de zero a vinte

Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.'''


nExt = ('um', 'dois', 'tres','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze','doze','treze','quatorze' or 'catorze', 'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
nInt = (int(input('Digite um numero inteiro (1 a 20): ')))
if nInt > 20 or nInt < 0:
    print('Numero invalido')
    exit()
nExt2 = nExt[nInt-1]
print(f'o numero digitado foi {nInt}, que em extenso é {nExt2}')