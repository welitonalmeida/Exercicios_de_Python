print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 or r3 < r1 + r2:
    print('OS segmentos {}, {} e {} PODEM FORMAR TRIÂNGULO!'.format(r1, r2, r3))
else:
    print('Os segmentos {}, {} e {} NÃO PODEM FORMAR TRIÂNGULO!'.format(r1, r2, r3))
