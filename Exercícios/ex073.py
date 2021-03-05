times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição!')
