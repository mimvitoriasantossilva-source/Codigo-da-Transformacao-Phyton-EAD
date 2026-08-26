# 🍞 Sistema de Vendas - Padaria (CLI)

## 📌 Visão Geral e Histórias de Usuário (User Stories)

O ** Sistema de Vendas da Padaria** é uma aplicação interativa via linha de comando (CLI - *Command Line Interface*), desenvolvida em Python para gerenciar a comercialização de produtos, controle de estoque e atendimento ao cliente de forma direta no terminal.

### Visões dos Envolvidos:
- **PD (Dono do Negócio):** Deseja um sistema de vendas eficiente para a padaria, permitindo o controle de vendas e monitoramento dos produtos disponíveis.
- **QA (Cliente):** Busca facilidade e rapidez no processo de compra e suporte, economizando tempo e evitando filas.
- **Tech / Dev (Programador):** Implementação de funcionalidades essenciais (cadastro, busca, vendas, cancelamento e estoque) seguindo boas práticas de desenvolvimento de software.
- **UX (Designer de Experiência):** Foco em um menu de navegação intuitivo, claro e agradável no terminal.
- **IA (Análise de Dados):** Estrutura preparada para registro de transações que permitam a análise futura de padrões de consumo e faturamento.

---

## 🚀 Funcionalidades Principais

- **1. Cadastrar Produto:** Permite o cadastro de novos produtos (Nome, Descrição, Validade, Estoque e Preço) nas vagas disponíveis.
- **2. Listar Produtos:** Exibe todos os produtos atualmente cadastrados no estoque com suas respectivas informações detalhadas.
- **3. Excluir Produto:** Remove um produto do sistema filtrando pelo nome e liberando sua vaga.
- **4. Pesquisar Produto:** Consulta rápida da existência, localização e quantidade de um produto específico no estoque.
- **5. Realizar Venda:** Registra a venda de itens, calcula o valor total da compra e atualiza automaticamente o estoque disponível.
- **6. Suporte ao Cliente:** Canal integrado de atendimento com opções de central de ajuda, chat ao vivo e formulário de envio de mensagens.
- **7. Cancelar Venda:** Permite o estorno de vendas e devolve a quantidade especificada de itens de volta ao estoque.
- **0. Sair:** Encerra a execução do sistema com segurança.

---

## 🛠️ Tecnologias e Estruturas Utilizadas

### Linguagem
- **Python 3**

### Interface
- **CLI (Command Line Interface):** Execução 100% via terminal, sem dependência de bibliotecas de interface gráfica.

### Estruturas de Programação Utilizadas
- **Laços de Repetição (`while True`):** Mantém o menu principal ativo em loop até que o usuário escolha a opção de sair.
- **Estruturas Condicionais (`if`, `elif`, `else`):** Gerenciamento do fluxo de opções do menu e validação das regras de negócio (ex.: estoque insuficiente, vagas cheias, produto não encontrado).
- **Variáveis Locais e De Controle:** Armazenamento individual dos atributos de cada vaga de produto (`p1`, `p2`, `p3`).
- **Formatação de String e Emojis:** Uso de *f-strings* e formatação de valores monetários (`R$ {:.2f}`) para uma melhor legibilidade no terminal.
- **Tratamento de Strings (`.lower()`):** Garantia de busca e comparação de nomes sem sensibilidade a maiúsculas/minúsculas.

---

## 📋 Panorama Geral: O Sistema de Pedidos da Padaria

O **Sistema de Vendas da Padaria** foi projetado para resolver a necessidade de controle operacional básico de uma padaria de pequeno/médio porte de forma leve e rápida. 

Por ser um aplicativo CLI, não exige instalação de dependências pesadas ou ambientes gráficos complexos. O menu interativo orienta o atendente ou cliente em cada passo, permitindo realizar transações rapidamente, consultar preços, gerenciar a reposição e estornos de produtos e acessar canais de suporte em poucos comandos.

---

## 💻 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou copie o código do arquivo `main.py` (ou `padaria.py`).
3. Abra o seu terminal/prompt de comando no diretório do arquivo.
4. Execute o comando:
   ```bash
   python main.py