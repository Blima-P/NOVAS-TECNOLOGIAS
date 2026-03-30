# Desafio 1 - Higienização de Dados

def limpar_dados(lista):
    # Filtra apenas usuarios com status_ativo == True usando lambda e filter
    usuarios_ativos = list(filter(lambda usuario: usuario['status_ativo'] == True, lista))
    
    # nome em maiusculo e email em minusculo
    for usuario in usuarios_ativos:
        usuario['nome'] = usuario['nome'].upper()
        usuario['email'] = usuario['email'].lower()
    
    return usuarios_ativos

if __name__ == "__main__":
    # Banco de dados ficticio
    dados_brutos = [
        {'nome': 'João Silva', 'email': 'JOAO@EMAIL.COM', 'status_ativo': True},
        {'nome': 'maria santos', 'email': 'Maria@Email.com', 'status_ativo': True},
        {'nome': 'Pedro Lima', 'email': 'PEDRO@gmail.COM', 'status_ativo': False},
        {'nome': 'ana costa', 'email': 'ANA@HOTMAIL.com', 'status_ativo': True},
        {'nome': 'Carlos Souza', 'email': 'carlos@Yahoo.COM', 'status_ativo': False}
    ]
    
    print("DADOS ANTES DA LIMPEZA")
    for usuario in dados_brutos:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Ativo: {usuario['status_ativo']}")
    
    # Chama a funcao de limpeza
    dados_limpos = limpar_dados(dados_brutos)
    
    print("\nDADOS DEPOIS DA LIMPEZA    ")
    print("(Apenas usuarios ativos, nomes em MAIUSCULO, emails em minusculo)")
    for usuario in dados_limpos:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")
