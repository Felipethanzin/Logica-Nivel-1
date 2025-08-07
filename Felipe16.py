#16) As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade = int(input("Digite o número de maçãs compradas: "))


if quantidade < 12:
    preco_unitario = 1.30
else:
    preco_unitario = 1.00


custo_total = quantidade * preco_unitario


print(f"Custo total da compra: R${custo_total:.2f}")
