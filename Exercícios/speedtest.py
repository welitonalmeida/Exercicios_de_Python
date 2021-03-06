# pip install speedtest-cli
import speedtest

test = speedtest.Speedtest()
down = test.download()
upl = test.upload()
print(f"A velocidade de Download é: {down}.\nA velocide de Upload é {upl}.")
