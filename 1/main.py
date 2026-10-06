import json

with open(r"1\vendas.json") as arquivo:
    dados = json.load(arquivo)

comissoes = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]
    # Calcula a comissão
    if valor < 100:
        comissao = 0
    elif valor < 500:
        comissao = valor * 0.01
    else:
        comissao = valor * 0.05
    # Cria o vendedor na lista Comissoes
    if vendedor not in comissoes:
        comissoes[vendedor] = 0

    # Soma a comissão da venda ao total do vendedor naquele momento
    comissoes[vendedor] += comissao

# Mostra a comissão final para cada vendedor
for vendedor in comissoes:
    print(f"{vendedor}: R$ {comissoes[vendedor]:.2f}")
