import shutil
'''biblioteca uada para mover ou copiar arquivos'''
import os
'''biblioteca para criar pastas, checar caminhos e entre outros'''

arquivo_origem = "dados.txt" 
pasta_backup = "backup_destino"


if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)
    '''olha se a pasta backup_destino ja existe, caso nao exita o os.makedirs() cria a pasta no computador'''

caminho_destino = os.path.join(pasta_backup, arquivo_origem)
'''junta a pasta e o nome do arquivo para criar o caminho de forma correta'''

try:
    shutil.copy2(arquivo_origem, caminho_destino)
    '''copia o arquivo original para a pasta certa'''
    print(f"Backup realizado com sucesso! Arquivo copiado para: '{caminho_destino}'")
except FileNotFoundError:
    '''se o arquivo nao existir, ives de fechar o programa entra no except e mostra uma mensagem no terminal'''
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado para fazer o backup. Execute a atividade 1 primeiro!")