import csv
'''importa a biblioteca do python que é focada em manipular arquivos CSV'''

lista_notas = [
    ["Nome", "Nota1", "Nota2"], 
    ["Ana", "8.5", "9.0"],
    ["Bruno", "7.0", "6.5"],
    ["Carla", "9.5", "10.0"]
]

with open("notas_alunos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";")
    '''cria o obejto escritor, que é configurado para usar ponto e virgula para separar cada coluna.
    newline="" impede que o python coloque lihas em brancos entre os dados quando for salvar'''
    escritor.writerows(lista_notas)
    '''grava todas as linhas da lista de uma vez só demtro do arquivo CSV'''
print("Dados de notas salvos em notas_alunos.csv!")

print("\n--- Conteúdo carregado do CSV ---")
with open("notas_alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=";")
    '''cria o objeto leiotr para ler o aquivo por liha'''
    for linha in leitor:
        '''olha todo o arquivo e a cada volta, a variavel linha vira uma lista com itens'''
        print(f"Aluno: {linha[0]} | Notas: {linha[1:] if linha[1:] else 'Sem notas'}")