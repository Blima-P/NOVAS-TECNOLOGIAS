# Analisador de Texto
frase = input("Digite uma frase: ")

#deixa tudo em minusculo
frase = frase.lower()
#separa a frase em palavras
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1

total_palavras = len(palavras)

total_unicas = len(contagem)

print("\nPalavras que se repetem:")
tem_repetida = False
for palavra in contagem:
    if contagem[palavra] > 1:
        print(f"'{palavra}' aparece {contagem[palavra]} vezes")
        tem_repetida = True

if not tem_repetida:
    print("Nenhuma palavra se repete")

palavra_mais_frequente = ""
maior_contagem = 0

for palavra in contagem:
    if contagem[palavra] > maior_contagem:
        maior_contagem = contagem[palavra]
        palavra_mais_frequente = palavra


print("RELATÓRIO FINAL")
print(f"Total de palavras: {total_palavras}")
print(f"Palavras únicas: {total_unicas}")
print(f"Palavra mais frequente: '{palavra_mais_frequente}' ({maior_contagem} vezes)")

