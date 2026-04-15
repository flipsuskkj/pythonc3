'''a = 4
b = 5
s = a + b
print(s)
a = 8
b=9
s=a+b
print(s)
a=2
b=1
s = a + b
print(s)'''

'''def soma(a,b):
    s = args + args
    print(s)


soma(4,5)
soma(8,9)
soma(2,1)
soma(2,7)

def contador(*num):
    for v in num:
        print(f'{v} -> ', end='')
    print(sorted(num))
    print(f'Recebi os valores {num} e são ao todo {len(num)} elementos')

contador(1,15,29,34,5,23,7,999,9)'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

val = [6,3,9,1,0,2]
dobra(val)
print(val)


def soma(*vals):
    s = 0
    for v in vals:
        s += v
    print(f'a soma vale: {s}')


soma(5,2)
soma(2,9,4)
