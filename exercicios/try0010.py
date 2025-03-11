t = int(input('Tempo do seu carro: '))

if t < 3:
    print('Seu carro é novo')
else: 
    print('Seu carro é velho')


n = str(input('Qaul é o seu nome: ')).upper()
if n == 'JOSIAS':
    print('Que nome honrado meu caro ksksk')
else:
    print('Não é ruim, mas poderia ser melhor')

n1 = float(input('Nota: '))
n2 = float(input('Nota 2 : '))
m = (n1+n2) / 2

print('Sua média foi {}'.format(m))

if m >= 6:
    print('Parábens.')
else:
    print('Seria bom melhorar um pouco sua média')


