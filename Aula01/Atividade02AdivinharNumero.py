NUMERO_SECRETO = 42
MAX_TENTATIVAS = 5

acertou = False
tentativa = 1

while tentativa <= MAX_TENTATIVAS and not acertou:
    chute = int(input(f"Tentativa {tentativa}/{MAX_TENTATIVAS}: "))

    if chute < NUMERO_SECRETO:
        print("Muito baixo! Tente maior.")
    elif chute > NUMERO_SECRETO:
        print("Muito alto! Tente menor.")
    else:
        print("Correto!")
        acertou = True

    tentativa += 1

if not acertou:
    print(f"\nVocê perdeu! O número secreto era {NUMERO_SECRETO}.")
else:
    print(f"Parabéns! Você acertou na tentativa {tentativa - 1}!")
