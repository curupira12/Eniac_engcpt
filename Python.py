import random

numero_secreto = random.randint(1, 10)

print("🔢 Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

while True:
    chute = int(input("Digite seu palpite: "))

    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif chute < numero_secreto:
        print("🔼 Tente um número maior.")
    else:
        print("🔽 Tente um número menor.")
print("Obrigado por jogar!")
# Fim do jogo
# Você pode reiniciar o jogo executando o código novamente.

