# Remover livro

def remover_livro(dados, titulo):
    """
    Remove um livro do dicionário pelo título
    
    Args:
        dados (dict): Dicionário com os dados dos livros
        titulo (str): Título do livro a ser removido
        
    Returns:
        dict: Dicionário atualizado sem o livro especificado
    """
    dados["livros"] = [livro for livro in dados["livros"] 
                      if livro["titulo"].lower() != titulo.lower()]
    return dados



# Exemplos: 

import json


def carregar_dados_json(arquivo_json='livros.json'):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"livros": []}

def adicionar_livro(dados, titulo, autor, ano, preco):
    novo_livro = {
        "id": len(dados["livros"]) + 1,
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "preco": float(preco)
    }
    dados["livros"].append(novo_livro)
    return dados


if __name__ == "__main__":
    
    dados = carregar_dados_json()
    
    # Adiciona alguns livros
    dados = adicionar_livro(dados, "Dom Casmurro", "Machado de Assis", 1899, 29.90)
    dados = adicionar_livro(dados, "1984", "George Orwell", 1949, 39.90)
    dados = adicionar_livro(dados, "O Guarani", "José de Alencar", 1857, 34.50)
    
    print("Antes de remover:")
    print(json.dumps(dados, indent=4, ensure_ascii=False))
    
    # Remove livro pelo título 
    dados = remover_livro(dados, "1984")
    
    print("\nDepois de remover:")
    print(json.dumps(dados, indent=4, ensure_ascii=False))
    
    # Salva as alterações
    with open('livros.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
