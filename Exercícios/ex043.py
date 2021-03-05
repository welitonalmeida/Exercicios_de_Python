peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = (peso / (altura ** 2))
print('O IMC é  de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= imc < 25:
    print('Peso Ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade Mórbida!')
