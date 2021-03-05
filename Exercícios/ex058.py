from random import randint
from time import sleep
palp = 1
nivel = int(input('Níveis\n[1]Fácil\n[2]Médio\n[3]Difícil\nDigite o nível selecionado: '))
if nivel == 1:
    a = 0
    b = 5
    computador = randint(a, b)
    print('-=-' * 19)
    print('Vou pensar em um número entre {} e {}. Tente adivinhar...'.format(a, b))
    print('-=-' * 19)
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        palp += 1
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
    else:
        while jogador != computador:
            palp += 1
            jogador = int(input('Em que número eu pensei? '))
            print('PROCESSANDO...')
            sleep(1)
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
elif nivel == 2:
    a = 0
    b = 10
    computador = randint(a, b)
    print('-=-' * 19)
    print('Vou pensar em um número entre {} e {}. Tente adivinhar...'.format(a, b))
    print('-=-' * 19)
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        palp += 1
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
    else:
        while jogador != computador:
            palp += 1
            jogador = int(input('Em que número eu pensei? '))
            print('PROCESSANDO...')
            sleep(1)
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
elif nivel == 3:
    a = 0
    b = 15
    computador = randint(a, b)
    print('-=-' * 19)
    print('Vou pensar em um número entre {} e {}. Tente adivinhar...'.format(a, b))
    print('-=-' * 19)
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        palp += 1
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
    else:
        while jogador != computador:
            palp += 1
            jogador = int(input('Em que número eu pensei? '))
            print('PROCESSANDO...')
            sleep(1)
        print('Parabéns, acertou!')
        print('Você precisou de {} tentativas!'.format(palp))
else:
    print('Selecione um nível válido!')
