# Declaração da função 'área'
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é {a} m².')


# Programa principal
print(' Controle de Terrenos')
print('-'*22)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
