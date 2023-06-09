peso = float(input('Digite é o peso: (km)'))
altura = float(input('Digite a altura: (m)'))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print(f'Seu imc é de {imc:.2f}. Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu imc é de {imc:.2f}. Você está na faixa de peso ideal.')
elif 25 < imc <= 30:
    print(f'Seu imc é de {imc:.2f}. Você está com sobrepeso.')
elif 30 < imc <= 40:
    print(f'Seu imc é de {imc:.2f}. Você está com obesidade.')
else:
    print(f'Seu imc é de {imc:.2f}. Você está com obesidade mórbida.')
