n = int(input('Número: '))
c = 0

tot = 0
dv = 0
for c in range(1, n+1, 1):
    if n % c == 0:
        print('\033[33m', end=(' '))
        tot = tot + 1
    else: 
        print('\033[31m', end=(' '))
        dv = dv + 1 

    print('{}'.format(c),end=(' '))
    
print('A quantidade total de divisiveis foi {} e a de não divisiveis foi {}'.format(tot, dv))
if tot < 3:
    print('É primo')
else:
    print('Não é primo')