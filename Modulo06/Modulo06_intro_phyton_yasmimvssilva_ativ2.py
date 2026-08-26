import json
''' aqui importa a biblioteca do python responsavel por trabalhar com json.'''

clientes = {
    "cliente_1": {"nome": "Carlos Souza", "email": "carlos@email.com", "ativo": True},
    "cliente_2": {"nome": "Beatriz Lima", "email": "beatriz@email.com", "ativo": False}
}

with open("clientes.json", "w", encoding="utf-8") as arquivo_json:
    # indent=4 serve para deixar o arquivo visualmente organizado ("bonito")
    json.dump(clientes, arquivo_json, indent=4, ensure_ascii=False)
    '''aqui, esssa linha do codigo muda o dicionario clientes e muda direto para dentro do arquivo .json.
    o indent=4 faz com que o texto com espaços para facilitar a leitura para os humanos.
    o ensure_ascii=False deixa as letras que tem assento emvez d mudar para algo estranho'''
print("Dicionário salvo em clientes.json!")

with open("clientes.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)
    '''essa linha do codigo le o arquivo .json e muda o texto de volta para o dicionario em python na variavel dados_carregados'''

print("\n--- Dados carregados do JSON ---")
print(dados_carregados)