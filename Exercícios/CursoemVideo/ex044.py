print('=============LOJAS GUANABARA==============')
preco = float(input('Qual é o preço do produto? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2X de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 20/100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}X de R${parcela:.2f} com juros.')
else:
    total = preco
    print('Erro. Por favor, escolha uma opção de pagamento existente. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar RS{total} no final.')
