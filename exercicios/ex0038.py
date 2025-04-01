import datetime
at = datetime.date.today().year
print(at)
a = int(input('Ano de nascimento: '))
i = at - a
print('quem nasceu em {} está com {} em {}'.format(a, i, at))
g = input('Seu genero é M ou F: ')

if g == 'M':
    if i == 18: 
        print('Você deve se alistar imediatamente!!!')

    elif i < 18:
        print('ainda falta {} para o alistamento'.format((18 - i)))
        print('Seu alistamento será em {}'.format((a + 18)))

    elif i > 18:
        print('Você deveria ter se alistado há {} anos'.format(i - 18))
        print('seu alistamento foi em {}'.format(a + 18))

elif g == 'F':
    print('Você não precisa se alistar')