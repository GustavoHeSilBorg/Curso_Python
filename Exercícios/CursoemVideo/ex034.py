sal = float(input('Digite o salário do funcionário: R%'))
if sal > 1250.00:
    nsal1 = sal * 10/100
    print(f'O novo salário será de R${nsal1 + sal}.')
else:
    nsal2 = sal * 15/100
    print(f'O novo salário será de R${nsal2 + sal}.')
