dist = float(input('Qual a distância da viagem que pretende realizar em Km? '))
if dist <= 200:
    print(f'O valor da passagem será de R${dist * 0.5:.2f}.')
else:
    print(f'O valor da passagem será de R${dist * 0.45:.2f}')
