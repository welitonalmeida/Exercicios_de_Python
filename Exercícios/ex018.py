print('======= DESAFIO 18 =======')
'''import math
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, math.tan(math.radians(ang))))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f}° tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {:.1f}° tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {:.1f}° tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))
