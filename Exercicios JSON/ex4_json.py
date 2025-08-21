def buscar_livros_por_autor(dados, nome_autor):
    """
    Busca livros no dicionário por autor
    
    Args:
        dados (dict): Dicionário com os dados dos livros
        nome_autor (str): Nome do autor a ser buscado
        
    Returns:
        list: Lista de livros do autor especificado (pode ser vazia)
    """
    return [livro for livro in dados["livros"] 
            if nome_autor.lower() in livro["autor"].lower()]