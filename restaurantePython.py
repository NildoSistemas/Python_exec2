total = float(input("valor da conta  R$ "))
pessoas = int(input("Quantas pessoas"))
gorjeta = total * 10/100
por_pessoa = (total + gorjeta)/pessoas


print(f"Cada uma paga R$ {por_pessoa:.2f}")