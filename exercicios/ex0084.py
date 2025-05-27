rt = []
lf = []
glmr = glmn = []
c = 0
while True:
    rt.insert(0,str(input('Nome: ')))
    rt.insert(1,float(input('Peso: ')))
    if len(lf) == 0:
        mr = mn = rt[1]
    else:
        if rt[1] > mr:
            mr = rt[1]
        if rt[1] < mn:
            mn = rt[1] 
    r = str(input('Quer contnuar[S/N]: '))
    lf.append(rt[:])
    rt.clear()
    if r in 'Nn':
        break
for p in lf:
    if p[1] == mr:
        glmr.append(p[0][:])
    if p[1] == mn:
        glmn.append(p[0][:])
print(lf)
print(lf[0][1])
print(f'Você cadastrou {len(lf)} pessoas')
print(f'O maior peso foi {mr}', end=' [] ')
for p in lf:
    if p[1] == mr:
        print(f'{p[0]}', end=' [] ')
print('')
print(f'O menor peso foi {mn}', end=' [] ')
for p in lf:
    if p[1] == mn:
        print(f'{p[0]}', end=' [] ',)


    

    
