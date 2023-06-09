nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando notas {nota1:.1f} e {nota2:.1f}, a média do aluno é: {media:.1f}')
print('O aluno está:')
if media < 5:
    print('\33[31mREPROVADO!\33[0m')
elif 7 >= media <= 5:
    print('\33[33mRECUPERAÇÃO!\33[0m')
elif media >= 7:
    print('\33[32mAPROVADO!\33[0m')
