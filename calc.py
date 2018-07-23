# Calculadora em Python

def ent():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    return x,y

def soma(x, y):
    return x + y

def dim(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print('********** PyCalc **********')

print('\n\nDigite 1 para adição\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão\n\n')

inp = int(input('Qual operação desejas fazer: '))
while inp in range(1, 5):
    x, y = ent()
    if inp == 1:
        ret = soma(x, y)
        print('%d + %d = %d' %(x, y, ret))
    elif inp == 2:
        ret = dim(x, y)
        print('%d - %d = %d' % (x, y, ret))
    elif inp == 3:
        ret = mult(x, y)
        print('%d * %d = %d' % (x, y, ret))
    else:
        ret = div(x, y)
        print('%d / %d = %d' % (x, y, ret))
    inp = int(input('Qual operação desejas fazer: '))
else:
    print('Comando não existe!')
