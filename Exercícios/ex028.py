from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! Realmente pensei no {}!'.format(jogador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
