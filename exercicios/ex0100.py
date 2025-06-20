import random
def l(lp):
    for c in range(0, 5):
        lp.append(random.randint(0, 10))
def p(l):
    m = 0
    for c in l:
        if c % 2 == 0:
            m = m + c
    print(m)


n = []
l(n)
print(n)
p(n)