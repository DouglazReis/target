import datetime

# Pega o valor e arruma a vírgula caso o usuário digite
texto_valor = input("Digite o valor: R$ ")
texto_valor = texto_valor.replace(",", ".")
valor = float(texto_valor)

# Pega a data e separa em dia, mês e ano
texto_data = input("Digite a data de vencimento (DD/MM/AAAA): ")
pedacos_data = texto_data.split("/")
dia = int(pedacos_data[0])
mes = int(pedacos_data[1])
ano = int(pedacos_data[2])

# Cria a data de vencimento e pega o dia de hoje
data_vencimento = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

# Verifica se a conta passou do dia de hoje
if data_vencimento >= hoje:
    print("A conta não está atrasada.")
    print("Valor dos juros: R$ 0.00")
    print("Valor total: R$", round(valor, 2))
    
if data_vencimento < hoje:
    # Calcula quantos dias passaram
    diferenca = hoje - data_vencimento
    dias_atrasados = diferenca.days
    
    # Calcula os juros (2,5% é 0.025)
    juros_de_um_dia = valor * 0.025
    juros_total = juros_de_um_dia * dias_atrasados
    
    valor_total = valor + juros_total
    
    # Mostra o resultado na tela
    print("Dias de atraso:", dias_atrasados)
    print("Valor dos juros: R$", round(juros_total, 2))
    print("Valor total: R$", round(valor_total, 2))
    