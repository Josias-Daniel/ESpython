lista = []
pos = c = 0
while True:
    while c != 5:
        lista.append(input('Número para adicionar: '))
        lista.sort()
        if c == 0:
            mn = mr = lista[0]
        else:
            if lista[c] > mr:
                mr = lista[c]
            elif lista[c] < mn:
                mn = lista[c]
        for p ,v in enumerate(lista):
            if v == lista[c]:
                pos = p 
                print(pos, p, v)
        print(f'Número {lista[c]} colocado na posição {pos}')
        print(lista)
        c = c + 1
        p = v = 0
    break