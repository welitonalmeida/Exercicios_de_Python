num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))

operação = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n\nO que deseja faze? '))
if operação == 1:
    soma = num1 + num2
    print('\nA soma de {} e {} é igual a {}!'.format(num1, num2, soma))

elif operação == 2:
    multiplicação = num1 * num2
    print('\nA multiplicação entre {} e {} é {}!'.format(num1, num2, multiplicação))
elif operação == 3:
    if num1 > num2:
        maior = num1
        print('\nO {} é maior!'.format(maior))
    elif num1 < num2:
        maior = num2
        print('\nO {} é maior!'.format(maior))
    else:
        print('\nSão iguais!')
elif operação == 4:
    while operação == 4:
        num1 = int(input('\nDigite um valor: '))
        num2 = int(input('Digite um valor: '))

        operação = int(input(
            '\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n\nO que deseja faze? '))
        if operação == 1:
            soma = num1 + num2
            print('\nA soma de {} e {} é igual a {}!'.format(num1, num2, soma))
        elif operação == 2:
            multiplicação = num1 * num2
            print('\nA multiplicação entre {} e {} é {}!'.format(num1, num2, multiplicação))
        elif operação == 3:
            if num1 > num2:
                maior = num1
                print('\nO {} é maior!'.format(maior))
            elif num1 < num2:
                maior = num2
                print('\nO {} é maior!'.format(maior))
            else:
                print('\nSão iguais!')
        elif operação == 5:
            print('\nSaindo agora!')
        else:
            print('Opção inválida!')
elif operação == 5:
    print('\nSaindo agora!')
else:
    print('Opção inválida!')
