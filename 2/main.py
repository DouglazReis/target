import json

arquivo = open(r"2\estoque.json")
dados = json.load(arquivo)

id_movimento = 1
rodando = True

while rodando == True:
    codigo = int(input("Digite o código do produto (0 para sair): "))

    if codigo == 0:
        rodando = False
    else:
        tipo = input("Digite entrada ou saída: ")
        quantidade = int(input("Digite a quantidade: "))
        descricao = input("Digite a descrição da movimentação: ")

        achou_produto = False

        for produto in dados["estoque"]:
            if produto["codigoProduto"] == codigo:
                achou_produto = True

                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero.")
                else:
                    if tipo == "entrada":
                        produto["estoque"] = produto["estoque"] + quantidade

                        print("\nID da movimentação:", id_movimento)
                        print("Descrição:", descricao)
                        print("Produto:", produto["descricaoProduto"])
                        print("Estoque final:", produto["estoque"], "\n")

                        id_movimento = id_movimento + 1

                    elif tipo == "saída" or tipo == "saida":
                        if quantidade > produto["estoque"]:
                            print("Estoque insuficiente.")
                        else:
                            produto["estoque"] = produto["estoque"] - quantidade

                            print("\nID da movimentação:", id_movimento)
                            print("Descrição:", descricao)
                            print("Produto:", produto["descricaoProduto"])
                            print("Estoque final:", produto["estoque"], "\n")

                            id_movimento = id_movimento + 1
                    else:
                        print("Tipo de movimentação inválido.")

        if achou_produto == False:
            print("Produto não encontrado.")