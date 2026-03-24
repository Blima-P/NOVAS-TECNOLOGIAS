#Desafio: Inventário de Loja

#lista de produtos em estoque.
estoque = [
    {"nome": "Celular", "preco": 1889.90, "quantidade": 15},
    {"nome": "Teclado Mecânico", "preco": 250.00, "quantidade": 3},
    {"nome": "Televisão", "preco": 899.90, "quantidade": 2},
    {"nome": "Mouse", "preco": 120.00, "quantidade": 0},
    {"nome": "Webcam", "preco": 199.90, "quantidade": 0},
    {"nome": "Caixa de Som", "preco": 150.00, "quantidade": 8},
]
valor_total = 0

print("INVENTÁRIO DA LOJA")
print("\nProdutos com valor acima de R$ 500:")

#valor total em estoque e produtos com valor acima de R$ 500.
for produto in estoque:
    
    valor = produto["preco"] * produto["quantidade"]
  
    valor_total = valor_total + valor

    if valor > 500:
        print(f"- {produto['nome']}: R$ {valor:.2f}")

print(f"\nValor total em estoque: R$ {valor_total:.2f}")

produtos_em_falta = [produto["nome"] for produto in estoque if produto["quantidade"] == 0]

print("\nProdutos em falta no estoque:")
for nome in produtos_em_falta:
    print(f"- {nome}")

print("\nFim do relatório")
