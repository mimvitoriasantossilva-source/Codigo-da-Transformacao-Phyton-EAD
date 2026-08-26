conteudo_para_salvar = "Olá! Este é um texto de teste armazenado em um arquivo TXT usando Python."
'''A gente usa o with open para abrir ou criar um aquivo chamados dados.txt.
O "w" a gente usa para que caso o arquivo ja exista, ele sobrescreve o conteudo e caso nao exista, ele cria um novo..
'''
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_para_salvar) 
    '''escreve o texto que esta na variavel conteudo_para_salvar dentro do aquivo.'''
print("Arquivo TXT criado e salvo com sucesso!")
'''mostra ma mensagem no terminal para confirmar que a etapa de escrita terminou'''

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    '''abre o  dados.txt de novo, mas agora no modo de leitura.'''
    conteudo_lido = arquivo.read()
    '''le todo o texto que esta no arquivo de uma vez só e salva na variavel conteudo_lido'''

print("\n--- Conteúdo lido do arquivo TXT ---")
print(conteudo_lido)
'''diz no termial o texto que foi lido '''