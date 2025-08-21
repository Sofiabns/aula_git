# Filtragem por produto

def filtrar_vendas_por_produto(vendas, nome_produto):
    return [venda for venda in vendas if venda['produto'] == nome_produto]

# Exemplo de uso
vendas = [
    {'produto': 'Coxinha', 'valor_venda': 100},
    {'produto': 'Coca-cola', 'valor_venda': 200},
    {'produto': 'Coxinha', 'valor_venda': 150},
    {'produto': 'Empada', 'valor_venda': 300},
]

resultado = filtrar_vendas_por_produto(vendas, 'Coxinha')
print("Vendas do Produto A:", resultado)    
