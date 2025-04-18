n = str(input('Sexo [M/F]: ')).strip().upper()[0]
while n not in 'MmFf':
    n = str(input('Sexo invalido insira novamente. Sexo [M/F]: ')).strip().upper()[0]

print('Sexo {} cadastrado'.format(n))