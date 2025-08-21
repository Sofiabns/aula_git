# Leitura de Dados:

import csv

def ler_dados_csv(caminho_arquivo):
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        dados = [linha for linha in leitor_csv]  # Lê as linhas e armazena numa lista
    return dados

# Ler o arquivo csv
caminho_arquivo = 'arquivo1.csv' 
dados = ler_dados_csv(caminho_arquivo)

# Imprimir os dados lidos
for linha in dados:
    print(linha)
