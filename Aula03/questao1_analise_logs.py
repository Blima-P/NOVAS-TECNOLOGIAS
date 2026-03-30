logs = [
    "2023-10-01 10:00:00 INFO User 105 logged in",
    "2023-10-01 10:05:23 ERROR Database connection failed",
    "2023-10-01 10:07:00 INFO User 105 requested /home",
    "2023-10-01 10:15:00 WARNING Memory usage above 80%",
    "2023-10-01 10:20:00 ERROR Timeout on API gateway",
    "2023-10-01 10:22:00 INFO User 202 logged in"
]


def analisar_logs(lista_logs):
    # função que analisa uma lista de logs e conta quantos de cada tipo existem.
    # dicionario vazio
    contagem = {}

    for linha in lista_logs:
        # uso o split() para separar a string em partes
        partes = linha.split()
        
        # O nível de severidade está na posição 2 (índice começa em 0)
        # Posição 0: data, Posição 1: hora, Posição 2: nível
        nivel = partes[2]
        
        # Se o nível já existe no dicionário, incremento +1
        # Se não existe ainda, começo contando como 1
        if nivel in contagem:
            contagem[nivel] = contagem[nivel] + 1
        else:
            contagem[nivel] = 1
            
    return contagem

if __name__ == "__main__":
    # Chamo a função passando a lista de logs
    resultado = analisar_logs(logs)
    
    print(f"Dicionário completo: {resultado}")
    print()
