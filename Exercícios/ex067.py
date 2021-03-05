while True:
    n = int(input('Quer ver a tabuada de quanto? '))
    print('-'*37)
    if n == 0 or n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 37)
print('Programa tabuada encerrado.')
