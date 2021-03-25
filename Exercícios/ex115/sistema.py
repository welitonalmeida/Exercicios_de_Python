from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # LISTAR O CONTEÚDO DE UM ARQUIVO!
        lerarquivo(arq)
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
