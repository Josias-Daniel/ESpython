r = 0 
rsn = ''
r = input('Diga um número: ')
mr = r   
mn = r 
rsn = str(input('Quer continuar: '))
while rsn != 'N':
    r = input('Diga um número: ')
    if r > mr:
        mr = r
    elif r < mn:
        mn = r
    rsn = str(input('Quer continuar: '))

print('Número maior {}, número menor {}'.format(mr,mn))
