l = []
c = 0
while True:
    l.append(int(input('Número: ')))
    r = str(input('Continuar[S/N]:  '))
    if r in 'Nn':
        break
l.sort(reverse = True)
print(l)

if 5 in l:
    print('O número 5 está na lista')
    print('OBAAAA')
else:
    print('O número 5 NÃO está na lista')