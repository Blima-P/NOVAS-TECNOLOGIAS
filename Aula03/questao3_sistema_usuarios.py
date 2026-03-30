class Usuario:
    def __init__(self, id, nome, email):
        # atributos privados (o __ na frente impede acesso direto de fora)
        # encpsular
        self.__id = id
        self.__nome = nome
        
        # Para o email, uso o setter para já fazer a validação
        # Se o email for inválido, o setter vai mostrar erro
        self.__email = None  
        self.set_email(email)   
    # Getters são métodos para ACESSAR os atributos privados de forma segura
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    
    # Setters são métodos para MODIFICAR os atributos privados de forma segura
    
    def set_id(self, novo_id):
        self.__id = novo_id
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_email(self, novo_email):#verifica se tem @ de acordo com a regra de negocio
        if "@" in novo_email:
            self.__email = novo_email
        else:
            print(f"E-mail inválido: '{novo_email}' não contém @")#se nao tiver @ mostra erro 
    
    def __str__(self):
        return f"Usuario(id={self.__id}, nome='{self.__nome}', email='{self.__email}')"


class GerenciadorUsuarios:#lista de usuarios
    def __init__(self):
        self.__usuarios = []  # Lista privada de usuários
    
    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print(f"Usuário '{usuario.get_nome()}' adicionado com sucesso!")
    
    def remover_usuario_por_id(self, id):
        # Percorro a lista procurando o usuário com o ID informado
        for usuario in self.__usuarios:
            if usuario.get_id() == id:
                self.__usuarios.remove(usuario)
                print(f"Usuário com ID {id} removido com sucesso!")
                return 
        #usuario nao encontrado
        print(f"Usuário com ID {id} não encontrado!")
    
    def listar_usuarios(self):
        if len(self.__usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return
        print("Lista de Usuários")
        for usuario in self.__usuarios:
            print(f"  - {usuario}")

if __name__ == "__main__":
    print("Criando usuários")
    
    # Crio alguns usuários
    user1 = Usuario(1, "Maria Silva", "maria@email.com")
    user2 = Usuario(2, "João Santos", "joao@empresa.com.br")
    user3 = Usuario(3, "Ana Costa", "ana_costa@gmail.com")
    
    print()
    print("Testando email inválido")
    # Tento criar usuário com email inválido
    user4 = Usuario(4, "Pedro Lima", "pedro.sem.arroba")
    
    print()
    print("Usando o Gerenciador")
    
    gerenciador = GerenciadorUsuarios()
    gerenciador.adicionar_usuario(user1)
    gerenciador.adicionar_usuario(user2)
    gerenciador.adicionar_usuario(user3)
    
    print()
    gerenciador.listar_usuarios()
    print()
    print("Removendo usuário")
    gerenciador.remover_usuario_por_id(2)
    
    print()
    # Listo novamente para ver que foi removido
    gerenciador.listar_usuarios()
    print()
    print("Usando Getters e Setters")
    print(f"Nome do user1: {user1.get_nome()}")
    user1.set_nome("Maria Silva Santos")
    print(f"Nome atualizado: {user1.get_nome()}")
