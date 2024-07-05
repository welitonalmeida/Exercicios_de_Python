# pip install speedtest-cli
import speedtest

teste = speedtest.teste()
down = teste.download()
upl = teste.upload()
print(f"A velocidade de Download é: {down}.\nA velocidade de Upload é {upl}.")

