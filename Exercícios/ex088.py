from time import sleep
from random import randint
lista = list()
jogos = list()
tot = 0
print('"'*32)
print(' '*6, 'Jogo da MEGA SENA', ' '*6)
print('"'*32)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS ', '=-'*3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*16)
print('-'*8, '< BOA SORTE! >', '-'*8)
print('-='*16)
