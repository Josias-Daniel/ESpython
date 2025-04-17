cq = 0
md = 0
for c in range(1 ,4+1, 1):
    cq = cq + 1
    nomeat = str(input('Nome da {}* pessoa: '.format(cq)))
    idadeat = int(input('Idade: '))
    sexoat = str('Sexo [M/F]')
    md = md + idadeat / 3
    
print(md)