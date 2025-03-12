import random
import time

n = int(input('Digite um número de 1-2: '))

print('PROCESSANDO')
time.sleep(2)

nr = random.randint(1, 2)

print('Eu escolhi {}'.format(nr))

if n == nr:
    print('Você acertou seu pão de queijo')
else:
    print('Você errou seu pão SEM queijo')