r = 0 
rsn = ''
r = input('Diga um número: ')
mr = r   
mn = r 
rsn = str(input('Quer continuar: ')).upper().strip()[0]

while rsn in  'Ss':
    r = input('Diga um número: ')
    if r > mr:
        mr = r
    if r < mn:
        mn = r
    rsn = str(input('Quer continuar: ')).upper().strip()[0]
    if rsn != 'S':
        if rsn != 'N':
            print('Algo errado')
            rsn = 'S'


print('Número maior {}, número menor {}'.format(mr,mn))
