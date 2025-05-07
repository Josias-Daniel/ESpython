while True:
    nt = int(input('Quer ver a tabuada de qual número: '))
    if nt < 0 :
        break
    else:
        c = 0
        while c < 10:
            c = c + 1
            rt = nt * c
            print(f'{nt} X {c} = {rt}')
print('PROGRAMA ENCERRADO.')