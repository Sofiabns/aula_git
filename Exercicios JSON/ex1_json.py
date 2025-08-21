# Carregar dados de um arquivo JSON

import json

def carregar_dados_json(arquivo_json='livros.json'):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"livros": []} 