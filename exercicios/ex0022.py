NC = str(input('Nome: ')).strip()

print('Seu nome Maiúsculo fica {}'.format(NC.upper()))

print('Seu nome Minúsculo fica {}'.format(NC.lower()))

print('O tanto de letras do seu noe é {}'.format(len(NC)-NC.count(' ')))

PN = NC.split()

print('Seu primeiro nome é {} e tem {} letras'.format(PN[0],len(PN[0])))
