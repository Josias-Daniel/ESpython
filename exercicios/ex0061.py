n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
t = n1
c = 1
while c <= 10:
    print('{} --D'.format(t), end=(' '))
    t = t + n2
    c = c + 1

print('FIM')
