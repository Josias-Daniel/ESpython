cq = 0
md = 0
Mvelho = 0 
Fnova = 0
Hnome = 'nada'
for c in range(1 ,4+1, 1):
    cq = cq + 1
    nomeat = str(input('Nome da {}* pessoa: '.format(cq)))
    idadeat = int(input('Idade: '))
    sexoat = str(input('Sexo [M/F]'))
    md = md + idadeat / 4
    if idadeat > Mvelho and sexoat == 'M':
        Mvelho = idadeat
        Hnome = nomeat
        print('FOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
    if sexoat == 'F' and idadeat <= 20:
        Fnova = Fnova + 1
print('O total de mulheres com menos/ou 20 anos é de {}'.format(Fnova)) 
print('O Homem mais velho é {} com {} anos'.format(Hnome, Mvelho)) 
print('A média de idade é de {}'.format(md))