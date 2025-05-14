pl = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM','PYTHON','CURSO','GRATIS',
      'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MARCADOR', 'PROGRAMADOR', 'FUTURO')
for pos in pl:
    print(f'\nNa palavra {pos}, temos', end=': ')
    for lt in pos:
        if lt.lower() in 'aeiou':
            print(lt, end=' ')