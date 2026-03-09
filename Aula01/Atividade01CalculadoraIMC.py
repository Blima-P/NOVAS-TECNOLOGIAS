nome = input("Qual o seu nome? ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = round(peso / (altura ** 2), 2)

print(f"\nOlá, {nome}!")
print(f"Seu IMC é: {imc}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Classificação: {classificacao}")
