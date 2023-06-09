'''co = float(input('Comprimento do cateto oposto?: '))
ca = float(input('Comprimento do cateto adjacente?: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hip:.2f}.')'''

import math
co = float(input('Comprimento do cateto oposto?: '))
ca = float(input('Comprimento do cateto adjacente?: '))
hip = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}.')

from math import hypot
co = float(input('Comprimento do cateto oposto?: '))
ca = float(input('Comprimento do cateto adjacente?: '))
hip = hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}.')

