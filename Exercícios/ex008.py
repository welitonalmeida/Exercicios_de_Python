print('======= DESAFIO 08 =======')
m = float(input('Uma disância em metros: '))
print('A medida de {}m corresponde a: '.format(m))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format((m / 1000), (m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)))
