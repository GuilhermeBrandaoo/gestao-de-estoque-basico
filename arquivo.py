# Usei dicionário aninhado para guardar o valores (nome, quantidade e preço)
produtos = {
    "produto1": {
        "nome": "Arroz",
        "quantidade": 1,
        "preco": 39.99
    },
    "produto2": {
        "nome": "Feijão",
        "quantidade": 12,
        "preco": 29.99
    },
    "produto3": {
        "nome": "Carne",
        "quantidade": 20,
        "preco": 59.99
    },
}

resposta = ""

while resposta != "4":
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do sistema")
    resposta = input("Digite um número: ");
    if resposta == "4":
        break