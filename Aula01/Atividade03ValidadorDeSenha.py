while True:
    senha = input("Digite uma senha: ")

    tem_tamanho = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)

    if tem_tamanho and tem_numero and tem_maiuscula:
        print("Senha válida!\n")
        break
    else:
        print("Senha inválida! Verifique os requisitos:")
        if not tem_tamanho:
            print("Deve ter pelo menos 8 caracteres")
        if not tem_numero:
            print("Deve conter pelo menos um número")
        if not tem_maiuscula:
            print("Deve conter pelo menos uma letra maiúscula")
        print()

print("=" * 40)
print("   RELATÓRIO DE SEGURANÇA")
print("=" * 40)

tamanho = len(senha)
print(f"Tamanho da senha: {tamanho} caracteres")

qtd_letras = sum(1 for char in senha if char.isalpha())
print(f"Letras: {qtd_letras}")

qtd_numeros = sum(1 for char in senha if char.isdigit())
print(f"Números: {qtd_numeros}")

qtd_especiais = sum(1 for char in senha if not char.isalnum())
print(f"Caracteres especiais: {qtd_especiais}")

if tamanho <= 9:
    nivel = "Fraca"
elif tamanho <= 12:
    nivel = "Média"
else:
    nivel = "Forte"

print(f"\nNível de segurança: {nivel}")

#usei IA nessa porem foi uso conciente a fins de aprendizado.