# Desafio 2 - Gerenciador de Frota / Locadora de Equipamentos

class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"
    
    def alugar(self):
        self.status = "Alugado"
    
    def devolver(self):
        self.status = "Disponível"


class Locadora:
    def __init__(self):
        self.inventario = [] 
        self.faturamento_por_cliente = {} 
    
    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)
    
    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        # Procura o equipamento pelo id
        for equipamento in self.inventario:
            if equipamento.id_equipamento == id_equipamento:
                if equipamento.status == "Disponível":
                    # Calcula o custo
                    custo = equipamento.preco_diaria * dias
                
                    equipamento.alugar()
                    
                    # Atualiza o faturamento do cliente
                    if nome_cliente in self.faturamento_por_cliente:
                        self.faturamento_por_cliente[nome_cliente] += custo
                    else:
                        self.faturamento_por_cliente[nome_cliente] = custo
                    
                    print(f"Locacao realizada! {nome_cliente} alugou {equipamento.nome} por {dias} dias. Total: R${custo:.2f}")
                    return True
                else:
                    print(f"Equipamento {equipamento.nome} nao esta disponivel.")
                    return False
        
        print(f"Equipamento com id {id_equipamento} nao encontrado.")
        return False
    
    def equipamentos_disponiveis(self):
        # Retorna lista com nomes dos equipamentos disponiveis
        disponiveis = []
        for equipamento in self.inventario:
            if equipamento.status == "Disponível":
                disponiveis.append(equipamento.nome)
        return disponiveis

if __name__ == "__main__":
    locadora = Locadora()
    furadeira = Equipamento(1, "Furadeira", 25.00)
    serra = Equipamento(2, "Serra Circular", 45.00)
    betoneira = Equipamento(3, "Betoneira", 80.00)
    locadora.cadastrar_equipamento(furadeira)
    locadora.cadastrar_equipamento(serra)
    locadora.cadastrar_equipamento(betoneira)
    
    print("EQUIPAMENTOS DISPONIVEIS")
    print(locadora.equipamentos_disponiveis())
    
    print("\n REALIZANDO LOCACOES")
    locadora.realizar_locacao("João", 1, 3)  
    locadora.realizar_locacao("Maria", 2, 2)
    locadora.realizar_locacao("João", 3, 1)
    
    print("\nEQUIPAMENTOS DISPONIVEIS AGORA")
    print(locadora.equipamentos_disponiveis())
    
    print("\nFATURAMENTO POR CLIENTE")
    for cliente, total in locadora.faturamento_por_cliente.items():
        print(f"{cliente}: R${total:.2f}")
    
    print("\nDEVOLVENDO EQUIPAMENTO")
    furadeira.devolver()
    print(f"Furadeira devolvida! Status: {furadeira.status}")
    
    print("\nEQUIPAMENTOS DISPONIVEIS APOS DEVOLUCAO")
    print(locadora.equipamentos_disponiveis())
