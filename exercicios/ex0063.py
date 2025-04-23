n = int(input('Número: '))
c = 0
f = 0 
f1 = 1
print('--{}--{}'.format(f,f1),end=(''))
while c < n - 1:
    c = c + 1
    f2 = f1 + f
    print('--{}'.format(f2),end=(''))
    f = f1 
    f1 = f2

