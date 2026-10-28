<h1 align="center">
  📋 API - Gerenciador de Tarefas
</h1>

<p align="center">
  Uma API RESTful simples, eficiente e direta ao ponto para gerenciamento de tarefas (To-Do List), desenvolvida em <strong>Python</strong> com <strong>FastAPI</strong> e gerenciada via <strong>Poetry</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry" />
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status" />
</p>

---

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar o Projeto](#-como-executar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo a passo](#passo-a-passo)
- [Rotas da API](#-rotas-da-api)
  - [1. Adicionar Tarefa](#1-adicionar-tarefa)
  - [2. Listar Tarefas](#2-listar-tarefas)
  - [3. Concluir Tarefa](#3-concluir-tarefa)
  - [4. Remover Tarefa](#4-remover-tarefa)
- [Documentação Interativa (Swagger)](#-documentação-interativa-swagger)
- [Autor](#-autor)

---

## 💡 Sobre o Projeto

O **Gerenciador de Tarefas** é uma API REST desenvolvida com o intuito de praticar conceitos fundamentais do ecossistema Python moderno para desenvolvimento backend:
- Criação e roteamento com **FastAPI**;
- Manipulação de métodos HTTP (**POST**, **GET**, **PUT**, **DELETE**);
- Tratamento de parâmetros via **Query Strings**;
- Respostas e tratamento de erros customizados com **HTTPException** (ex: retorno `404` para recursos inexistentes);
- Gerenciamento de dependências e ambientes virtuais com **Poetry**.

---

## ✨ Funcionalidades

- [x] **Criar tarefa**: cadastra uma nova tarefa com nome, descrição e status de conclusão (padrão: `False`).
- [x] **Listar tarefas**: retorna todas as tarefas registradas em memória com seus respectivos IDs.
- [x] **Atualizar status**: busca a tarefa pelo nome e atualiza seu status para concluída (`True`).
- [x] **Remover tarefa**: localiza a tarefa pelo nome e realiza a exclusão da lista.
- [x] **Validação e erros**: lança erro `404 Not Found` caso tente atualizar ou remover uma tarefa inexistente.

---

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/) (versão 3.12+)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web de alta performance
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI ultrarrápido
- [Poetry](https://python-poetry.org/) - Gerenciador de dependências e empacotamento

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- Um cliente HTTP para testes como [Insomnia](https://insomnia.rest/), [Postman](https://www.postman.com/) ou o próprio navegador via Swagger.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/theycallmejohnnie/api-gerenciador-tarefas-python.git
   cd api-gerenciador-tarefas-python
   ```

2. **Instale as dependências com o Poetry:**
   ```bash
   poetry install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```bash
   poetry run uvicorn app:app --reload
   ```

4. **Acesse a API:**
   O servidor estará ativo em: `http://127.0.0.1:8000`

---

## 📌 Rotas da API

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/adiciona` | Cadastra uma nova tarefa |
| `GET` | `/tarefas` | Retorna todas as tarefas |
| `PUT` | `/atualiza` | Marca a tarefa indicada como concluída |
| `DELETE` | `/remove` | Deleta uma tarefa da lista |

---

### 1. Adicionar Tarefa
- **Método:** `POST`
- **URL:** `/adiciona`
- **Query Params:**
  - `nome_tarefa` (string, obrigatório)
  - `descricao_tarefa` (string, obrigatório)
  - `tarefa_concluida` (booleano, opcional, default: `false`)

**Exemplo de Requisição:**
```text
POST /adiciona?nome_tarefa=Estudar%20FastAPI&descricao_tarefa=Aprender%20rotas%20REST&tarefa_concluida=false
```

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa adicionada com sucesso!",
  "id": 1,
  "tarefa": {
    "nome_tarefa": "Estudar FastAPI",
    "descricao_tarefa": "Aprender rotas REST",
    "tarefa_concluida": false
  }
}
```

---

### 2. Listar Tarefas
- **Método:** `GET`
- **URL:** `/tarefas`

**Exemplo de Resposta (200 OK):**
```json
{
  "Lista de tarefas": {
    "1": {
      "nome_tarefa": "Estudar FastAPI",
      "descricao_tarefa": "Aprender rotas REST",
      "tarefa_concluida": false
    }
  }
}
```

---

### 3. Concluir Tarefa
- **Método:** `PUT`
- **URL:** `/atualiza`
- **Query Params:**
  - `nome_tarefa` (string, obrigatório)

**Exemplo de Requisição:**
```text
PUT /atualiza?nome_tarefa=Estudar%20FastAPI
```

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa atualizada com sucesso!",
  "id": 1,
  "tarefa": {
    "nome_tarefa": "Estudar FastAPI",
    "descricao_tarefa": "Aprender rotas REST",
    "tarefa_concluida": true
  }
}
```

*(Se a tarefa não existir, retornará status `404` com `{"detail": "Tarefa não encontrada na lista"}`).*

---

### 4. Remover Tarefa
- **Método:** `DELETE`
- **URL:** `/remove`
- **Query Params:**
  - `nome_tarefa` (string, obrigatório)

**Exemplo de Requisição:**
```text
DELETE /remove?nome_tarefa=Estudar%20FastAPI
```

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa removida com sucesso!"
}
```

*(Se a tarefa não existir, retornará status `404` com `{"detail": "Tarefa não encontrada na lista"}`).*

---

## 📖 Documentação Interativa (Swagger)

O FastAPI gera automaticamente uma interface web interativa para testar todas as rotas diretamente do navegador sem precisar de ferramentas externas:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 👤 Autor

Desenvolvido por **Jhonatan Sousa**.

- GitHub: [@theycallmejohnnie](https://github.com/theycallmejohnnie)
- Email: [jhonatansousa354@gmail.com](mailto:jhonatansousa354@gmail.com)

---

<p align="center">
  Feito com ☕ e Python!
</p>

