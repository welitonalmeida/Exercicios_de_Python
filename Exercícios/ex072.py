from time import sleep
cont = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','catorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente! ')
print('Saindo em ',end='')
print('3... ',end='')
sleep(2)
print('2... ',end='')
sleep(2)
print('1... ',end='')
sleep(2)
print('ZERO!')
