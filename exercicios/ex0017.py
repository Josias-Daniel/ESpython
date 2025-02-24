'''N1 = float(input('cateto oposto: '))
N2 = float(input('Cateto Adjacente: '))
H = (N1**2 + N2**2) ** (1/2)
print('A hipotenuza vai medir {:.2f}'.format(H))'''

import math
N1 = float(input('cateto oposto: '))
N2 = float(input('Cateto Adjacente: '))
H = math.hypot(N1, N2)
print('A hipotenuza é {:.5f} '.format(H))