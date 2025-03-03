import random
N1 = str(input('Primeiro Aluno '))
N2 = str(input('Segundo Aluno '))
N3 = str(input('Terceiro Aluno '))
N4 = str(input('Quarto Aluno '))
LDP = [N1,N2,N3,N4]
PE = random.choice(LDP)
print('O escolhido para a tarefa foi {}'.format(PE))