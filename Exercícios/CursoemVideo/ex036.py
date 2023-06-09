valor = float(input('Digite é o valor do imóvel:R$ '))
salario = float(input('Digite o salário do comprador:R$ '))
anos = int(input('Em quantos anos deseja pagar: '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print(f'Parabéns, compra aprovada! O valor mensal da prestação será de:R${prestacao:.2f}')
else:
    print(f'Compra não aprovada. Infelizmente, o valor mensal da prestação solicitado de R${prestacao:.2f}, está acima do percentual permitido.')
