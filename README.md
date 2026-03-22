# wsBackend-Fabrica26.1
# Grimoire - Backend (Fábrica 26.1)

Este é o serviço de backend do projeto **Grimoire**, desenvolvido como um **Projeto de Extensão Universitária**. A aplicação utiliza **Django 6.0.3** e é totalmente containerizada com **Docker**, focando na criação de um ecossistema robusto para o gerenciamento de dados e integração com serviços externos.

## 🛠️ Stack Técnica Detalhada

* **Framework:** Django 6.0.3
* **Linguagem:** Python 3.14.0
* **API Engine:** Django REST Framework 3.17.0
* **Infraestrutura:** Docker & Docker Compose (Base: `python:3.14-slim`)
* **Banco de Dados:** SQLite (Persistido via Volumes do Docker)

## 🌟 Funcionalidades Implementadas

* **Gestão de Casas:** Organização e listagem de entidades (Ex: Gryffindor, Slytherin) através do modelo `Casa`.
* **CRUD de Membros:** Sistema completo para cadastrar, listar, editar e deletar registros de bruxos vinculados a casas.
* **Consumo de API Externa:** Integração com a `hp-api` via biblioteca `requests` para exibição de dados dinâmicos.
* **Interface Administrativa:** Painel de controle otimizado para gestão de dados e usuários.

## 🏗️ Arquitetura do Sistema

O projeto aplica padrões consolidados de Engenharia de Software:

* **MVT (Model-View-Template):** Separação clara entre a camada de dados (`models.py`), lógica de negócio (`views.py`) e interface (`templates`).
* **Otimização Docker:** Uso de `.dockerignore` e variáveis de ambiente (`PYTHONUNBUFFERED=1`) para logs em tempo real e builds mais rápidos.

## 🚀 Como Executar o Projeto

A utilização do Docker garante um ambiente isolado e reprodutível.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/PedroHFL2006/wsBackend-Fabrica26.1](https://github.com/PedroHFL2006/wsBackend-Fabrica26.1)
    cd wsBackend-Fabrica26.1
    ```

2.  **Suba os containers:**
    ```powershell
    docker-compose up -d
    ```
    *Este comando constrói a imagem, aplica as migrações de banco de dados e inicia o servidor.*

3.  **Acesse no Navegador:**
    * **Dashboard principal:** `http://localhost:8000/wizards/`
    * **Personagens Oficiais (API):** `http://localhost:8000/personagens-hp`
    * **Painel Administrativo:** `http://localhost:8000/admin`

## 📂 Endpoints Disponíveis

| Rota              |                 Função                    |
| :---              | :---                                      |
| `/wizards/`       | Lista membros e casas cadastradas.        |
| `/cadastro/`      | Abre o formulário de novo bruxo.          |
| `/editar/<id>/`   | Edita informações de um membro existente. |
| `/deletar/<id>/`  | Remove permanentemente um registro.       |
| `/personagens-hp` | Lista dados dinâmicos da HP-API.          |
