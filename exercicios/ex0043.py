p= float(input('Peso: '))
alt = float(input('Aultura: '))
imc = p / (alt ** 2)
print('O pso dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')

elif imc > 18.5 and imc < 25:
    print('Peso ideal')

else:
    print('Sobrepeso')