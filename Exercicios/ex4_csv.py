# Gravar resultados em arquivo:

import csv

def gravar_resultados(total_vendas, vendas_filtradas, arquivo_saida='resultado_vendas.csv'):
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escreve cabeçalho
        writer.writerow(['RELATÓRIO DE VENDAS POR PRODUTO'])
        writer.writerow([])  # Linha em branco
        
        # Escreve o total
        writer.writerow(['Total Geral de Vendas:', f'R$ {total_vendas:.2f}'])
        writer.writerow([])  # Linha em branco
        
        # Escreve cabeçalho das vendas
        writer.writerow(['Vendas do Produto Específico:'])
        if vendas_filtradas:
            writer.writerow(vendas_filtradas[0].keys())  # Cabeçalho dos campos
        
        # Escreve cada venda
        for venda in vendas_filtradas:
            writer.writerow(venda.values())


# Dados de exemplo
vendas = [
    {'produto': 'Notebook', 'valor_venda': 3500.00, 'data': '01/01/2023'},
    {'produto': 'Mouse', 'valor_venda': 150.50, 'data': '02/01/2023'},
    {'produto': 'Notebook', 'valor_venda': 4200.00, 'data': '03/01/2023'},
    {'produto': 'Teclado', 'valor_venda': 250.75, 'data': '04/01/2023'}
]

# Calcula total e filtra
total = sum(v['valor_venda'] for v in vendas)
vendas_notebook = [v for v in vendas if v['produto'] == 'Notebook']

# Grava resultados
gravar_resultados(total, vendas_notebook)

