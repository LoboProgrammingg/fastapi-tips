# Mini CRM API com FastAPI (v1.0.0)

Este projeto é uma API simples de Gerenciamento de Contatos (CRM) desenvolvida em **FastAPI** para demonstrar boas práticas de desenvolvimento, arquitetura modular e fluxos de trabalho do Git/GitHub.

---

## 🚀 Funcionalidades Principais (v1.0.0)

* **CRUD Completo:** Criação, Leitura (individual e em lista), Atualização (PUT e PATCH) e Exclusão de Contatos.
* **Consultas Avançadas:** Paginação (`limit`/`offset`), Ordenação (`sort_by`/`direction`) e Filtros.
* **Arquitetura Modular:** Estrutura organizada com módulos para Routers, Models e Core (Configuração, Logging).
* **Robustez e Monitoramento:** Logging estruturado, Middleware para Request ID (rastreamento) e Exception Handlers customizados.
* **Segurança:** Proteção de endpoints de modificação via `X-API-Key` (Dependência).

## 🛠️ Como Executar Localmente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO-CONTA-A/mini-crm-fastapi.git](https://github.com/SEU-USUARIO-CONTA-A/mini-crm-fastapi.git)
    cd mini-crm-fastapi
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Crie o arquivo `.env`** (Recomendado para secrets):
    ```
    API_KEY_SECRET=super-secreta-chave-de-teste
    ```
5.  **Inicie o Servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    A API estará acessível em `http://127.0.0.1:8000`.

## 🔗 Documentação

A documentação interativa (Swagger UI) está disponível em `http://127.0.0.1:8000/docs`.