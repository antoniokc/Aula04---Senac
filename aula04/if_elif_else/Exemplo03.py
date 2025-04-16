# Entrada
tempo_filiacao = int(input('qual seu tempo na cooperativa? '))
vl_mov = float(input("Qual o valor movimentado nos ultimos 6 meses? "))


# Processamento
TEMPO_MINIMO = 3
LIMITE_MOV = 5000.0

if tempo_filiacao >= TEMPO_MINIMO or vl_mov > LIMITE_MOV:
    print('Sucesso!, o senhor(a) tem acesso ao beneficio especial')
else:
    print("Informamos que infelizmente o senhor(a) não tem acesso a beneficio")
