import math 
N1 = float(input('Número de graus'))
S = math.sin(math.radians(N1))
COS = math.cos(math.radians(N1))
TAN = math.tan(math.radians(N1))
print('O seno é {:.2f} o Conseno é {:.2f} e a Tangente tem valor de {:.2f}'.format(S, COS, TAN))