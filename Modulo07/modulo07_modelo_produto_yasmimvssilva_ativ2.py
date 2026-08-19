import datetime

print("--- Calculadora de Dias de Vida e Idade ---\n")

data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")

data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y")

hoje = datetime.datetime.now()

diferenca = hoje - data_nascimento

anos = diferenca.days // 365

print("\n--- Resultado ---")
print(f"🗓️ Data de hoje: {hoje.strftime('%d/%m/%Y')}")
print(f"⏳ Você já viveu aproximadamente {diferenca.days} dias!")
print(f"🎉 Sua idade aproximada é: {anos} anos.")