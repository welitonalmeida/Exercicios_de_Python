casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,\na prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação  <= minimo:
    print('Empréstimo \033[34mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')