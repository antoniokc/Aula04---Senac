codigo = int(input('Digite o Codigo para a área desejada: '))

match codigo:
    case 1:
        print('Acesso Liberado para a Academia')
    case 2:
        print('Acesso liberado para a piscina')
    case 3:
        print('Acesso liberado para a Salão de Festas')
    case 4:
        print('Acesso liberado para a Cobertura VIP')
    case 5 | 6:
        print('Acesso liberado para a Estacionamento')
    case 7 | 8 | 9:
        print('Acesso liberado para as áreas Comuns')
    case 10:
        print('Acesso liberado para a Administração')
    case 11:
        print('Acesso Tecnico')
    case _:
        print('Acesso Negado')
