vel = float(input('Qual a velocidade do carro? '))
velmax = 80
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado por excesso de velocidade. O limite permitido é de 80 Km/h.')
    print(f'A multa vai custar R${multa}.')
print('Tenha um bom dia! Dirija com segurança.')
