def salvar_dados_json(dados, arquivo='livros_atualizados.json'):
    """
    Salva os dados em um arquivo JSON
    
    Args:
        dados (dict): Dicionário com os dados a serem salvos
        arquivo (str): Nome do arquivo de saída
    """
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


import json




if __name__ == "__main__":
    
    dados = carregar_dados_json('livros.json')
    
    
    if not dados["livros"]:
        dados = adicionar_livro(dados, "Dom Casmurro", "Machado de Assis", 1899, 29.90)
        dados = adicionar_livro(dados, "Memórias Póstumas", "Machado de Assis", 1881, 35.50)
        dados = adicionar_livro(dados, "1984", "George Orwell", 1949, 39.90)
    
   
    livros_machado = buscar_livros_por_autor(dados, "Machado de Assis")
    print("Livros de Machado de Assis:")
    for livro in livros_machado:
        print(f"- {livro['titulo']} ({livro['ano']}) - R${livro['preco']:.2f}")
    
    
    salvar_dados_json(dados)
    print("\nDados salvos em 'livros_atualizados.json'")
