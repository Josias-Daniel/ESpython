import datetime
i = 0
padult = 0
pmenor = 0
anot = datetime.date.today().year
print(anot)
cp = 0
for c in range(1, 7+1):
    cp = cp + 1
    i = int(input('Ano de nascimento da {}* pessoa: '.format(cp)))
    f = anot - i
    print('{}'.format(c))
    if f >= 18:
        padult = padult + 1
    else:
        pmenor = pmenor + 1
    
print('O tanto de pessoas adultas foram {} e menores são {}'.format(padult,pmenor))
