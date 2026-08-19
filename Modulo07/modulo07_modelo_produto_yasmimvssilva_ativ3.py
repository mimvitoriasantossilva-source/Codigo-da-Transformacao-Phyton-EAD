import random
import math

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número secreto entre 1 e 100!\n")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite o seu palpite: "))
    tentativas += 1

    if chute < numero_secreto:
        print("💡 Dica: O número secreto é MAIOR!\n")
    elif chute > numero_secreto:
        print("💡 Dica: O número secreto é MENOR!\n")
    else:
        print("\n🎉 PARABÉNS! Você acertou!")
        print(f"Número de tentativas: {tentativas}")
    
        pontuacao = math.ceil(100 / tentativas)
        print(f"Sua pontuação final foi: {pontuacao} de 100 pts!")
        break