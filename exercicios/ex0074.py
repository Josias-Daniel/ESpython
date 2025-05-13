import random
ns = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),random.randint(0, 10), random.randint(0, 10))
c = 0
m = n = ns[0]
while True:
    if ns[c] > m:
        m = ns[c]
    if ns[c] < n:
        n = ns[c]
    c = c + 1
    if c == 5:
        break
print(ns)
print(f'Maior númrto {m}, menor número {n}')