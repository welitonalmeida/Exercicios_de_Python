from lib.interface import *
from time import sleep
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        sleep(1)
        cabeçalho('Saindo do Sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
