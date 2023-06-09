from datetime import date
atual = date.today().year
ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - ano_nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('A categoria de acordo com sua idade é MIRIM')
elif idade <= 14:
    print('A categoria de acordo com sua idade é INFANTIL')
elif idade <= 19:
    print('A categoria de acordo com sua idade é JUNIOR')
elif idade <= 25:
    print('A categoria de acordo com sua idade é SÊNIOR')
else:
    print('A categoria de acordo com sua idade é MASTER')
