'''cire um programa com uma tupla com várias palavras.('sem acentos')
Depois disso mostrar todas as suas vogais'''

pals = (
    str(input('Digite uma palavra: ')),
    'python', 'programacao', 'computador', 'teclado',
    'monitor', 'internet', 'software', 'hardware',
    'desenvolvimento', 'algoritmo', 'variavel', 'funcao',
    'estrutura', 'dados', 'sistema', 'rede', 'servidor',
    'cliente', 'aplicacao', 'codigo'
)

vog = 'aeiou'

for pal in pals:
    print(f'\nNa palavra \'{pal}\' temos: ', end='')

    # Verificando vogais
    for letra in pal:
        if letra in vog:
            print(letra, end=' ')