import datetime

ano = int(input('Ano: (0 para ano atual) '))
if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    vrb = str('Bissxesto')
else:
    vrb = str('não Bissexto')

anot = 0

if ano == datetime.date.today().year:
    print('Este é o ano tual e ele é {}'.format(vrb))
else:
    print('O ano é {}'.format(vrb))
print(datetime.date.today().year)