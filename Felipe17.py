#17) Classificação de Idade - Peça ao usuário sua idade e classifique da seguinte forma:
#Menor de 12 anos: Criança
#Entre 12 e 17 anos: Adolescente
#Entre 18 e 59 anos: Adulto
#60 anos ou mais: Idoso

idade = int(input("Digite sua idade: "))


if idade < 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"


print(f"Classificação: {classificacao}")
