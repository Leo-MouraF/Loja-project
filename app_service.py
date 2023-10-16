import json
from uuid import uuid4



def gerar_novo_produto(data):
    name = str(data.get("nome"))
    preco = data.get("valor")
    description = str(data.get("descricao"))
    category = str(data.get("categoria"))
    novo_produto = {
        "id": str(uuid4()),
        "nome": name,
        "preco": preco,
        "descricao": description,
        "categoria": category,
    }

    produtos_json = ler_o_json()
    escrever_no_json(produtos_json, novo_produto)

    return novo_produto


def escrever_no_json(produtos, novo_produto):
    with open("data/produtos.json", "w", encoding="utf-8") as arquivo_produtos:
        produtos[novo_produto["id"]] = novo_produto
        novo_produto_json = json.dumps(produtos, indent=4, ensure_ascii=False)
        arquivo_produtos.write(novo_produto_json)


def ler_o_json():
    with open("data/produtos.json", "r") as arquivo_produtos:
        produtos_dicionario = json.load(arquivo_produtos)
        return produtos_dicionario