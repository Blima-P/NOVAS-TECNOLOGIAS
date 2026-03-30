transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]
todas_categorias = []

# Percorro cada transação e pego só a categoria (posição 1 da tupla)
for transacao in transacoes:
    categoria = transacao[1]
    todas_categorias.append(categoria)
# O set automaticamente remove as duplicatas!
categorias_unicas = set(todas_categorias)

print(f"Todas as categorias (com repetição): {todas_categorias}")
print(f"Categorias únicas (usando set): {categorias_unicas}")
print()

totais_por_categoria = {}

for transacao in transacoes:
    # desempacoto a tupla em variáveis separadas
    id_transacao = transacao[0]
    categoria = transacao[1]
    valor = transacao[2]
    
    #se a categoria já existe no dicionário
    if categoria in totais_por_categoria:
        # se já existe, somo o valor atual ao que já tinha
        totais_por_categoria[categoria] = totais_por_categoria[categoria] + valor
    else:
        # se não existe, crio a chave com o primeiro valor
        totais_por_categoria[categoria] = valor
print(f"Dicionário de totais: {totais_por_categoria}")
