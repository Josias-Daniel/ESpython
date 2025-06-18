def cont(a, b, c):
        if a > b:
            c = -c
        elif b > a:
            c = +c
        for n in range(a, b, c):
            print(n, end=' ')
        print('FIM!' )


cont(1, 10, 1)
cont(10, 0, 2)
print('SUA CONTAGEM:')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
cont(a, b, c)


