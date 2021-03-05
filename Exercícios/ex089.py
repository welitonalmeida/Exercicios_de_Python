from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 12)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 23)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 50)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    print()
    if opc == 999:
        print('FINALIZANDO...')
        print()
        sleep(2)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMRE >>>')
