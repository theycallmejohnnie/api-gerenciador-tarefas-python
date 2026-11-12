<h1 align="center">
  📋 API - Gerenciador de Tarefas
</h1>

<p align="center">
  Uma API RESTful simples, eficiente e direta ao ponto para gerenciamento de tarefas (To-Do List), desenvolvida em <strong>Python</strong> com <strong>FastAPI</strong>, validação de esquemas via <strong>Pydantic</strong>, autenticação <strong>HTTP Basic</strong> e gerenciada com <strong>Poetry</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic" />
  <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry" />
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status" />
</p>

---

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Modelo de Dados (Schema)](#-modelo-de-dados-schema)
- [Autenticação](#-autenticação)
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
- Criação e roteamento com **FastAPI** seguindo convenções e boas práticas **RESTful** (recursos no plural e verbos HTTP semânticos);
- Modelagem, tipagem estática e validação de dados através do **Pydantic** (`BaseModel`);
- Manipulação completa dos principais métodos HTTP (**POST**, **GET**, **PUT**, **DELETE**);
- Envio e validação de dados no corpo da requisição (**Request Body** em JSON);
- Armazenamento em memória baseado em lista de objetos Python tipados (`list[Tarefa]`), mantendo as instâncias de `Tarefa` sem conversão desnecessária em dicionários;
- Localização e manipulação de tarefas pelo campo `nome_tarefa` (com suporte tanto a **Path Parameters** quanto a **Query Strings**);
- Paginação completa de resultados com parâmetros `page` e `limit`, além de ordenação flexível via `ordenar_por` (`nome_tarefa` ou `id`);
- Camada de segurança com autenticação **HTTP Basic** (`HTTPBasic`) e verificação de credenciais em tempo constante com `secrets.compare_digest` para mitigar ataques de temporização (*timing attacks*);
- Geração segura de identificadores sequenciais únicos via contador incremental, prevenindo colisões ou sobrescrita de dados após exclusões;
- Respostas estruturadas e tratamento de erros customizados com **HTTPException** (ex: retornos `401 Unauthorized` e `404 Not Found`);
- Gerenciamento de dependências e ambientes virtuais com **Poetry**.

---

## ✨ Funcionalidades

- [x] **Criar tarefa**: cadastra uma nova tarefa a partir de um corpo JSON validado (`nome_tarefa`, `descricao_tarefa` e `tarefa_concluida` com default `False`), armazenando a instância de `Tarefa` diretamente em uma lista em memória.
- [x] **Listar tarefas com paginação e ordenação**: retorna as tarefas paginadas através dos parâmetros `page` e `limit`, com suporte a ordenação por nome ou ID (`ordenar_por`) e metadados detalhados (página atual, total de páginas, etc.).
- [x] **Autenticação HTTP Basic**: proteção de todas as rotas com autenticação segura via `HTTPBasic` e credenciais validadas criptograficamente.
- [x] **Atualizar status**: busca a tarefa pelo seu nome (`nome_tarefa`) e atualiza seu status para concluída (`True`).
- [x] **Remover tarefa**: localiza a tarefa pelo seu nome (`nome_tarefa`) e realiza sua exclusão da lista.
- [x] **Identificador único e seguro**: geração incremental de IDs atribuídos diretamente a cada objeto `Tarefa`, evitando repetições ou sobrescritas após exclusões.
- [x] **Validação e erros**: validação automática dos dados de entrada com Pydantic e lançamento de códigos de status semânticos (`401` para credenciais inválidas e `404` para tarefas não encontradas).

---

## 📐 Modelo de Dados (Schema)

A entidade principal da aplicação é modelada através do Pydantic:

```python
class Tarefa(BaseModel):
    id: Optional[int] = None
    nome_tarefa: str
    descricao_tarefa: str
    tarefa_concluida: bool = False
```

| Campo | Tipo | Obrigatório | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `int` | Não (gerado na criação) | Identificador numérico único da tarefa |
| `nome_tarefa` | `str` | Sim | Nome ou título da tarefa |
| `descricao_tarefa` | `str` | Sim | Detalhes ou descrição da tarefa |
| `tarefa_concluida` | `bool` | Não (default: `false`) | Status de conclusão da tarefa |

---

## 🔐 Autenticação

Todas as rotas da API são protegidas por autenticação **HTTP Basic**. É necessário enviar as credenciais no cabeçalho `Authorization` da requisição:

| Chave | Valor Padrão |
| :--- | :--- |
| **Usuário** | `admin` |
| **Senha** | `admin` |

- **No Swagger UI (`/docs`):** Clique no botão verde **"Authorize"** no canto superior direito, insira o usuário `admin` e senha `admin`, e confirme.
- **Em clientes HTTP (cURL, Insomnia, Postman):** Utilize a aba/tipo **Basic Auth** informando o usuário e a senha.
- **Caso não autenticado:** A API responderá com status `401 Unauthorized`:
  ```json
  {
    "detail": "Credenciais inválidas"
  }
  ```

---

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/) (versão 3.14+)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web de alta performance
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados e definições de esquemas
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI ultrarrápido
- [Poetry](https://python-poetry.org/) - Gerenciador de dependências e empacotamento

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- [Python 3.14+](https://www.python.org/downloads/)
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

> 🔒 *Todas as rotas exigem autenticação HTTP Basic (`admin:admin`).*

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/tarefas` | Cadastra uma nova tarefa na lista |
| `GET` | `/tarefas` | Retorna tarefas com suporte a paginação e ordenação |
| `PUT` | `/tarefas/{nome_tarefa}` | Marca a tarefa indicada pelo nome como concluída |
| `DELETE` | `/tarefas/{nome_tarefa}` | Deleta uma tarefa da lista pelo nome |

---

### 1. Adicionar Tarefa
- **Método:** `POST`
- **URL:** `/tarefas`
- **Autenticação:** `Basic Auth` (`admin:admin`)
- **Corpo da Requisição (Body JSON):**
  ```json
  {
    "nome_tarefa": "Estudar FastAPI",
    "descricao_tarefa": "Aprender rotas REST e modelos Pydantic",
    "tarefa_concluida": false
  }
  ```
  > *Nota: O campo `tarefa_concluida` é opcional e possui valor padrão `false`.*

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa adicionada com sucesso!",
  "id": 1,
  "tarefa": {
    "id": 1,
    "nome_tarefa": "Estudar FastAPI",
    "descricao_tarefa": "Aprender rotas REST e modelos Pydantic",
    "tarefa_concluida": false
  }
}
```

---

### 2. Listar Tarefas
- **Método:** `GET`
- **URL:** `/tarefas`
- **Autenticação:** `Basic Auth` (`admin:admin`)
- **Query Params:**
  - `page` (inteiro, opcional, default: `1`, mínimo: `1`) - Número da página desejada
  - `limit` (inteiro, opcional, default: `10`, mínimo: `1`, máximo: `100`) - Quantidade de tarefas por página
  - `ordenar_por` (string, opcional, default: `"nome_tarefa"`) - Campo pelo qual a lista será ordenada (`"nome_tarefa"` ou `"id"`)

**Exemplo de Requisição:**
```text
GET /tarefas?page=1&limit=10&ordenar_por=nome_tarefa
```

**Exemplo de Resposta (200 OK):**
```json
{
  "pagina_atual": 1,
  "itens_por_pagina": 10,
  "total_tarefas": 1,
  "total_paginas": 1,
  "Lista de tarefas": [
    {
      "id": 1,
      "nome_tarefa": "Estudar FastAPI",
      "descricao_tarefa": "Aprender rotas REST e modelos Pydantic",
      "tarefa_concluida": false
    }
  ]
}
```

---

### 3. Concluir Tarefa
- **Método:** `PUT`
- **URL:** `/tarefas/{nome_tarefa}` *(também aceita via Query Param: `/tarefas?nome_tarefa=...`)*
- **Autenticação:** `Basic Auth` (`admin:admin`)
- **Parâmetro de Busca:**
  - `nome_tarefa` (string, obrigatório) - Nome da tarefa a ser concluída

**Exemplo de Requisição:**
```text
PUT /tarefas/Estudar%20FastAPI
```

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa atualizada com sucesso!",
  "tarefa": {
    "id": 1,
    "nome_tarefa": "Estudar FastAPI",
    "descricao_tarefa": "Aprender rotas REST e modelos Pydantic",
    "tarefa_concluida": true
  }
}
```

*(Se a tarefa não existir, retornará status `404 Not Found` com `{"detail": "Tarefa não encontrada na lista"}`).*

---

### 4. Remover Tarefa
- **Método:** `DELETE`
- **URL:** `/tarefas/{nome_tarefa}` *(também aceita via Query Param: `/tarefas?nome_tarefa=...`)*
- **Autenticação:** `Basic Auth` (`admin:admin`)
- **Parâmetro de Busca:**
  - `nome_tarefa` (string, obrigatório) - Nome da tarefa a ser removida

**Exemplo de Requisição:**
```text
DELETE /tarefas/Estudar%20FastAPI
```

**Exemplo de Resposta (200 OK):**
```json
{
  "message": "Tarefa removida com sucesso!"
}
```

*(Se a tarefa não existir, retornará status `404 Not Found` com `{"detail": "Tarefa não encontrada na lista"}`).*

---

## 📖 Documentação Interativa (Swagger)

O FastAPI gera automaticamente uma interface web interativa para testar todas as rotas diretamente do navegador sem precisar de ferramentas externas:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

> 💡 *No Swagger UI, utilize o botão **Authorize** informando o usuário `admin` e a senha `admin` antes de testar as rotas.*

---

## 👤 Autor

Desenvolvido por **Jhonatan Sousa**.

- GitHub: [@theycallmejohnnie](https://github.com/theycallmejohnnie)
- Email: [jhonatansousa354@gmail.com](mailto:jhonatansousa354@gmail.com)

---

<p align="center">
  Feito com ☕ e Python!
</p>
