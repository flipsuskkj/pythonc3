'''crie um programa onde vai ler uma expresão matematica e vai ler se os parenteses estão certos ou errados na ordem correta.'''

exp = input("Digite a expressão: ")
a = []

for simbolo in exp:
    if simbolo == '(':
        a.append('(')
    elif simbolo == ')':
        if len(a) > 0:
            a.pop()
        else:
            a.append(')')
            break

if len(a) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')