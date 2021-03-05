primeiro = int(input('Primeiro termo: '))
último = int(input('Último termo: '))
razão = int(input('Razão: '))
for c in range(primeiro, último + 1, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
