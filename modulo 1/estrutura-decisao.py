"""
    Todos os dias, somos confrontados com escolhas que parecem simples, mas
    carregam consigo consequências importantes na nossa rotina e no modo como
    encaramos o mundo!
"""

# estrutura condicional simples
# “Se isso acontecer, faça aquilo.”

idade = int(input("Qual sua idade: "))
if idade >= 18:
    print("Maior de idade")


temperatura = float(input("Digite a temperatura: "))
"""
    O programa verifica a condição (temperatura > 30). 
    Se essa condição for verdadeira (True), ele executa o comando que está dentro do if. 
    Caso seja falsa (False), o programa simplesmente continua sua execução normalmente, 
    sem executar nenhuma ação adicional
"""

if temperatura > 30:
 print("Está muito quente hoje!")


# estrutura condicional COMPOSTA
# “Se isso acontecer, faça isso.
# Senão, se for aquilo acontecer, faça aquilo”
valor_compra = float(input("Digite o valor da compra: R$ "))
"""
    A condição (valor_compra >= 100) é avaliada pelo programa. 
    Se for verdadeira, ele exibe a mensagem informando que o cliente tem direito ao desconto. 
    Caso seja falsa, o bloco do else é executado, informando que não há desconto disponível
"""

if valor_compra >= 100:
 print("Você ganhou um desconto de 10%!")
else:
 print("Sem desconto. Aproveite as próximas promoções!") 


# estrutura condicional ENCADEADA - "ANINHADA"
# "Se for isso, faça isso. Senão, se for aquilo,
# faça aquilo. Caso contrário, faça outra coisa.”

nota = float(input("Digite sua nota final: "))
if nota >= 9:
    print("Excelente desempenho!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")


# Parcelamento de acordo com o valor da Compra
#entrada de dados
valor = float(input("Digite o valor da Compra: "))

# condições
if valor <= 100:
    print("Pagamento à Vista")
    p = valor
else:
    if valor <= 200:
        print("Pagamento em 2x")
        p = valor / 2
    else:
        print("Pamento em 3x")
        p = valor / 3

# saida / exibição
print("O valor da cada parcela é: R$ ", p)