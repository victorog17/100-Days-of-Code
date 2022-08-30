# Calculado de gorjeta
print("Bem vindo a calculadora de gorjetas")
total_conta = float(input("Qual foi o valor total da conta?\n"))
total_pessoas = int(input("Quantas pessoas vão dividir a conta?\n"))
gorjeta = int(input("Qual percentual de gorgeta irá pagar? 10, 12 ou 15?\n"))
ajuste_gorjeta = (gorjeta / 100) + 1
conta_dividida = total_conta / total_pessoas
conta_com_gorjeta = conta_dividida * ajuste_gorjeta
print(f"Cada uma das {total_pessoas} deverá pagar R${conta_com_gorjeta:.2f}")