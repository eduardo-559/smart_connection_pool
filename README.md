# Smart Connection Pool

## 📌 Introdução
O **Smart Connection Pool** é um padrão de projeto que gerencia conexões com o banco de dados de forma eficiente, evitando desperdício de recursos e melhorando a escalabilidade do sistema. Ele permite que múltiplos clientes reutilizem conexões sem precisar criar novas a cada requisição.

## 👥 Equipe
- **Eduardo de Oliveira Sousa** – 510969  
- **Murilo dos Santos Cunha** – 521441  

## 🛠️ Tecnologias Utilizadas
- **Linguagem de programação:** Python  
- **Gerenciamento de concorrência:** Multithreading  
- **Estrutura de dados:** Fila (`queue.Queue`) para armazenar conexões disponíveis  
- **Testes automatizados:** `unittest` para validação das funcionalidades  
- **Versionamento de código:** Git e GitHub para controle de versão e colaboração  

## 📂 Estrutura do Projeto
```
smart_connection_pool/
│── src/                    # Código-fonte principal
│   │── __init__.py         # Arquivo para definir o pacote Python
│   │── database_connection.py  # Classe DatabaseConnection
│   │── connection_pool.py   # Classe ConnectionPool
│   │── client.py           # Classe Client
│── tests/                  # Testes unitários
│   │── test_connection_pool.py  # Arquivo para testes
│── examples/               # Exemplos de uso
│   │── example_1_webserver.py  # Exemplo 1: Servidor Web
│   │── example_2_reports.py    # Exemplo 2: Sistema de Relatórios
│   │── example_3_ecommerce.py  # Exemplo 3: E-commerce
│── docs/                   # Documentação do projeto
│   │── design_pattern.pdf  # Documento explicando o padrão
│── README.md               # Explicação geral do projeto
│── .gitignore              # Arquivos a serem ignorados no Git
```

## 🚀 Como Usar
### 📥 Clonando o repositório
```sh
git clone https://github.com/seu_usuario/smart_connection_pool.git
cd smart_connection_pool
```

### ▶️ Executando os exemplos
Para testar o funcionamento do pool de conexões, execute um dos exemplos disponíveis:

#### Exemplo 1: Servidor Web
```sh
python examples/example_1_webserver.py
```

#### Exemplo 2: Sistema de Relatórios
```sh
python examples/example_2_reports.py
```

#### Exemplo 3: E-commerce
```sh
python examples/example_3_ecommerce.py
```

### 🧪 Executando os Testes Automatizados
Para rodar os testes unitários, utilize o comando:
```sh
python -m unittest tests/test_connection_pool.py
```

## 📑 Documentação
O documento detalhado do **Smart Connection Pool** pode ser acessado [aqui](docs/design_pattern.pdf).

## 📌 Contribuição
Sinta-se à vontade para contribuir com melhorias! Para isso:
1. Faça um **fork** do repositório.
2. Crie uma nova **branch** para suas alterações.
3. Envie um **pull request** com as melhorias.

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

