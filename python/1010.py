valor_total = 0.0
for i in range(2):
    entrada = input().split()

    unidades = int(entrada[1])
    valor_peca = float(entrada[2])
    valor_total += valor_peca * unidades
    
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
