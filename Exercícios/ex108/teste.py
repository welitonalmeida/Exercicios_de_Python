import moeda

p = float(input('Digite o preço : R$'))
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 5%, temos {moeda.moeda(moeda.diminuir(p, 5))}')
