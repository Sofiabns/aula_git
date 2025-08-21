# Cálculo de total de vendas

import csv

def ler_dados_csv():
    with open('arquivo1.csv') as arquivo:
        return list(csv.DictReader(arquivo))

def calcular_total_vendas(dados):
    return sum(float(venda['valor_venda']) for venda in dados)

# Uso básico
vendas = ler_dados_csv()
total = calcular_total_vendas(vendas)
print(f"Total: R${total:.2f}")
