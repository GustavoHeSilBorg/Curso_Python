from random import choice # opção de usar a função randint, randint(0, 5)
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
num = int(input('Escolha um número entre 0 e 5: '))
print(f'Você escolheu o número: {num}.')
print('PROCESSANDO.......')
sleep(3)
if num == escolhido:
    print('VENCEU!!!')
else:
    print('PERDEU!!!')
print(f'Eu escolhi o número: {escolhido}. Tente novamente!')
#print('VENCEU!' if num == escolhido else 'PERDEU!')
