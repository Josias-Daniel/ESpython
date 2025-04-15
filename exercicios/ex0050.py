v = 0
for c in range(1, 6+1, 1):
    n = 0
    n = int(input('Diga numero {}: '.format(c)))
    if n % 2 == 0:
        v = v + n
print(v)