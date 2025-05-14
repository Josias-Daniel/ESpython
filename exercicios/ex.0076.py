mat =  ('lapis', 2,
        'boracha', 3,
        'Caderno', 5)
p = ('.' * 15)
for pos in range(0 ,len(mat)):
    if pos % 2 == 0:
        print(f'{mat[pos]}{p}', end='')
    else:
        print(f'{mat[pos]}')