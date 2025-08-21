# 2. Adicionar novo livro

def adicionar_livro(dados, titulo, autor, ano, preco):
    novo_livro = {
        "id": len(dados["livros"]) + 1, # Auto_increment
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "preco": float(preco)
    }
    dados["livros"].append(novo_livro)
    return dados