vl_da_compra = float(input('Qual o valor da compra meu caro: '))

# Constante usamos letra maiúscula
LIMITE = 250

if vl_da_compra > LIMITE:
    vl_final = vl_da_compra - (vl_da_compra * 0.16)
    print("Sua compra deu", vl_final, "já com desconto aplicado!")
else:
    print('Sua compra deu', vl_da_compra)
