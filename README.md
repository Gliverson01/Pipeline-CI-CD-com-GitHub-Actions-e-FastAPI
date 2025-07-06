# Pipeline CI/CD com GitHub Actions e FastAPI

Este projeto demonstra a implementação de um pipeline de Integração Contínua (CI) e Entrega Contínua (CD) para uma aplicação FastAPI, utilizando GitHub Actions para automação e Docker para conteinerização.

## Estrutura do Projeto

- `main.py`: Aplicação FastAPI de demonstração.
- `test_main.py`: Testes unitários para a aplicação FastAPI.
- `requirements.txt`: Dependências Python do projeto.
- `Dockerfile`: Define a imagem Docker para a aplicação.
- `.dockerignore`: Arquivos e diretórios a serem ignorados na construção da imagem Docker.
- `.github/workflows/main.yml`: Workflow do GitHub Actions para CI/CD.
- `.flake8`: Configuração para o linter Flake8.
- `todo.md`: Lista de tarefas do projeto.

## Pré-requisitos

Para executar este projeto localmente, você precisará ter instalado:

- Python 3.11+
- pip (gerenciador de pacotes Python)
- Docker
- Git

## Configuração Local

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd ci-cd-fastapi-project
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    pip install pytest flake8 black bandit
    ```

4.  **Execute os testes:**

    ```bash
    pytest
    ```

5.  **Execute o linter e o formatador:**

    ```bash
    flake8 .
    black .
    ```

6.  **Execute a verificação de segurança:**

    ```bash
    bandit -r . --exclude venv
    ```

7.  **Construa e execute a imagem Docker:**

    ```bash
    docker build -t fastapi-ci-cd-demo .
    docker run -d -p 8000:80 fastapi-ci-cd-demo
    ```

    A aplicação estará acessível em `http://localhost:8000`.

## Pipeline CI/CD com GitHub Actions

O arquivo `.github/workflows/main.yml` define o pipeline CI/CD que será executado automaticamente no GitHub Actions. Este workflow realiza as seguintes etapas:

-   **Checkout do Código**: Clona o repositório.
-   **Configuração do Python**: Configura o ambiente Python.
-   **Instalação de Dependências**: Instala as dependências do projeto.
-   **Execução de Testes**: Executa os testes unitários com `pytest`.
-   **Build e Push da Imagem Docker**: Constrói a imagem Docker da aplicação. (Atualmente configurado para não fazer push, mas pode ser habilitado para um registro de contêiner como Docker Hub ou GitHub Container Registry).

## Próximos Passos

-   Configurar o push da imagem Docker para um registro de contêiner.
-   Implementar a implantação contínua (CD) para um ambiente de nuvem (ex: AWS, Azure, GCP) usando Terraform.
-   Adicionar mais testes (integração, ponta a ponta).
-   Monitoramento e logging.



