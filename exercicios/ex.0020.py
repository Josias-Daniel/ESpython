import random
n1 = str(input('Nome 1'))
n2 = str(input('Nome 2'))
n3 = str(input('Nome 3'))
n4 =str(input('Nome 4'))
ldp = [n1,n2,n3,n4]
ord = random.shuffle(ldp)
print('A ordem será {}'.format(ldp))