import json

with open('dados.json') as f:
    dados = json.load(f)
    print(dados)
