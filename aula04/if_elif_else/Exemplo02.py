# Entrada
peso = float(input('informar o peso:'))
qtd_cx_estoque = int(input('Informar o estoque?')) 
pedido = int(input("Quantidade pedida: "))

# Processamento
LIMITE_PESO = 50

if qtd_cx_estoque >= pedido and peso < LIMITE_PESO:
    print('LIBERADO! seu pedido terá,', pedido,'caixas. Com um peso total de', peso ,"kg")
else:
    print('Pedido negado!')
