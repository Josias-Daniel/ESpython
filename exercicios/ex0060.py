n = int(input('Número fatorial: '))
c = 0
cf = 1
while not c == n:
    c = c + 1
    if c == 1:
        cf = c
        print(cf,'Oi')
    cf = (cf * c) 
    print(cf, end=(' X '))
print(cf)