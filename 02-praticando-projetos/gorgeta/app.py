valorConta = float(input("Digite o valor da conta >> "))
valorGorgeta = float(input("Digite o valor da Gorgeta >> "))

totalGorgeta = (valorConta * valorGorgeta) / 100
totalPagamento = totalGorgeta + valorConta

print(f"Valor da Gorgeta é {valorGorgeta} %")
print(f"Total a Pagar {totalPagamento}")
