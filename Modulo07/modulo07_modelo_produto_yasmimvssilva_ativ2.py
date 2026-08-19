import datetime

print("--- Calculadora de Dias de Vida e Idade ---\n")

data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")

try:
    # Converte a string para data
    data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    hoje = datetime.date.today()

    diferenca_dias = (hoje - data_nascimento).days
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    print("\n--- Resultado ---")
    print(f"🗓️ Data de hoje: {hoje.strftime('%d/%m/%Y')}")
    print(f"⏳ Você já viveu aproximadamente {diferenca_dias} dias!")
    print(f"🎉 Sua idade exata é: {idade} anos.")

except ValueError:
    print("\n⚠️ Erro: Digite a data no formato correto usando barras! Exemplo: 15/08/2000")