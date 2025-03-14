v = float(input('Velocidade do carro atual Km'))

m = (v - 120) * 7

if v <= 120: 
    print('Tenha um bom dia dirija com segurança')
else:
    print('Você está acima do limite, será multado em {}R$'.format(m))