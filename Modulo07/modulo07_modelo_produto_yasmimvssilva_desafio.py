import modulo07_yasmimvssilva_ativ1_utilidades as utilidades

print("=== DESAFIO EXTRA: SIMULAÇÃO DE PACOTE/MÓDULOS MULTIPLOS ===\n")

print("1. Executando funções importadas do Exercício 1 (utilidades):")
num1 = 20
num2 = 4

soma = utilidades.somar(num1, num2)
potencia = utilidades.potencia(num1, num2)

print(f"   -> Soma ({num1} + {num2}): {soma}")
print(f"   -> Potência ({num1} ^ {num2}): {potencia}\n")

print("2. Integração concluída com sucesso entre módulos do mesmo diretório!")