import random
x = random.randint(1,10)

print('Pensei em um número aleátorio entre 1 e 10 tente adivinhar')
r = int(input('Diga um número: ')) 
while not r == x:
    if r < x:
        r = int(input('Errou, um pouco mais: '))
    elif r > x:
        r = int(input('Errou, um pouco menos: '))
    



print('Parábens você acertou, o número é {}'.format(x))