#parametro
valor_kwh = 0.75
calculo_mes = 30 #mes comercial

print("\n-- Calculadora de Consumo Energético --")

#entrada de dados
nome_aparelho = input("Nome do aparelho (ex: Geladeira): ")
potencia = float(input(f"Potência de {nome_aparelho} em Watts (W): "))
horas_dia = float(input(f"Horas de uso por dia de {nome_aparelho} \n(ex: 2 horas e meia = 2.5 ou 2 horas = 2) "))


#processamento
# Fórmula: (Watts * horas * 30 dias) / 1000 para converter em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * valor_kwh

#exibição
print("-" * 40)
print(f"APARELHO: {nome_aparelho.upper()}")
print(f"CONSUMO ESTIMADO: {consumo_mensal:.2f} KWh/mês")
print(f"CUSTO ESTIMADO: R$ {custo_estimado:.2f}/mês")
print("-" * 40)
