# Acima de 07 APROVADO
# Entre 5 e 07 Recuperação
# Abaixo de 5 Reprovado


num = float(input('qual a nota do aluno: '))

if num >= 0:
    if num >= 7:
        print('Aprovado')
    elif num >= 5:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Valor Invalido')
