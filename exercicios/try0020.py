def mp(es):
    print(('=' * 30))
    print(es)
    print(('=' * 30))
def sm(a, b):
    s = a + b
    print(s)
def cont(*num):
        quan = len(num)
        print(f'{num} [são {quan} números]')
def db(l):
     pos = 0
     while pos < len(l):
          l[pos] = l[pos] * 2
          pos = pos + 1


vl = [0, 4, 8 , 9, 3, 5 ,6 , 232]
mp('melhor comida é:')
mp('PÃO DE QUEIJO')
sm(2339, 787439)
cont(90, 34, 52, 12, 47)
db(vl)
print(vl)
