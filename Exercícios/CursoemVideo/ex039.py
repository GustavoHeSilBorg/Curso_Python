from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'Você tem {idade} anos de idade. Ainda faltam {18 - idade} anos para se alistar.')
elif idade == 18:
    print('Você já completou 18 anos, está na hora de se alistar.')
else:
    print(f'Você já tem {idade} anos de idade. Já se passaram {idade - 18} anos do tempo de se alistar.')
