class JogoDaVelha:
    
    def __init__(self):
        # Uso espaço ' ' para representar posições vazias
        self.tabuleiro = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        # Jogador atual - 'X' sempre começa
        self.jogador_atual = 'X'
        # Contador de jogadas (máximo 9)
        self.jogadas = 0
    
    def mostrar_tabuleiro(self):
        # Mostra o tabuleiro no terminal de forma bonita e legível.
        print()
        print("    0   1   2")  # Números das colunas
        print("  +---+---+---+")
        
        for i in range(3):
            # Mostro o número da linha e o conteúdo
            print(f"{i} | {self.tabuleiro[i][0]} | {self.tabuleiro[i][1]} | {self.tabuleiro[i][2]} |")
            print("  +---+---+---+")
        print()
    
    def fazer_jogada(self, linha, coluna):
        #verifico se a posição está dentro dos limites (0 a 2)
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida! Use números de 0 a 2.")
            return False
        
        #verifico se a posição está vazia
        if self.tabuleiro[linha][coluna] != ' ':
            print("Essa posição já está ocupada! Escolha outra.")
            return False
        
        # se passou nas validações, faço a jogada
        self.tabuleiro[linha][coluna] = self.jogador_atual
        self.jogadas += 1
        
        # troca de turno de jogador
        if self.jogador_atual == 'X':
            self.jogador_atual = 'O'
        else:
            self.jogador_atual = 'X'
        
        return True
    
    def verificar_vencedor(self):
        tab = self.tabuleiro  
        # verifico as 3 LINHAS HORIZONTAIS
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] != ' ':
                return tab[i][0]
        # verifico as 3 COLUNAS VERTICAIS
        for j in range(3):
            if tab[0][j] == tab[1][j] == tab[2][j] != ' ':
                return tab[0][j]
        # Verifico a DIAGONAL PRINCIPAL (canto superior esquerdo ao inferior direito)
        if tab[0][0] == tab[1][1] == tab[2][2] != ' ':
            return tab[0][0]
        # Verifico a DIAGONAL SECUNDÁRIA (canto superior direito ao inferior esquerdo)
        if tab[0][2] == tab[1][1] == tab[2][0] != ' ':
            return tab[0][2]
        if self.jogadas == 9:
            return 'Empate'
        return None
    
    def jogar(self):
    #loop do jogo
        print("BEM-VINDO AO JOGO DA VELHA!")
        print("Jogador X começa!")
        print("Para jogar, digite a linha e coluna (0, 1 ou 2)")
        
        while True:
            self.mostrar_tabuleiro()
            print(f"Vez do jogador: {self.jogador_atual}")
            try:
                linha = int(input("Digite a linha (0-2): "))
                coluna = int(input("Digite a coluna (0-2): "))
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
                continue
            jogada_valida = self.fazer_jogada(linha, coluna)
            # Se a jogada não foi válida, volta para pedir outra
            if not jogada_valida:
                continue
            # Verifico se alguém ganhou
            resultado = self.verificar_vencedor()

            if resultado == 'Empate':
                self.mostrar_tabuleiro()
                print("=" * 40)
                print("   DEU VELHA! Empate!")
                print("=" * 40)
                break  # Sai do loop
            
            elif resultado is not None:
                self.mostrar_tabuleiro()
                print("=" * 40)
                print(f"   PARABÉNS! Jogador {resultado} venceu!")
                print("=" * 40)
                break  # Sai do loop
        
        # Pergunto se quer jogar novamente
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() == 's':
            # Crio um novo jogo e começo
            novo_jogo = JogoDaVelha()
            novo_jogo.jogar()

if __name__ == "__main__":
    # Crio uma instância do jogo e início
    jogo = JogoDaVelha()
    jogo.jogar()
