s = float(input('Sálario:'))
if s <= 1250:
    ns = s + (s * 15 / 100) 
else:
    ns = s + (s * 10 / 100)
print('Novo salário = {}'.format(ns))