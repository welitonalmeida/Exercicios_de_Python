from time import sleep
n = int(input('Digite um número para sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
    sleep(0.5)
