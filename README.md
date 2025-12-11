# 🏦 Crypto Analyst Agent (POC)

## 📌 Sobre o Projeto
Este projeto é uma **Prova de Conceito (POC)** desenvolvida para demonstrar a aplicação de **IA Agêntica e Generativa** em um contexto financeiro. 

O sistema atua como um **Agente Analista de Mercado**, orquestrando dados estruturados em tempo real (via API da Binance) com a capacidade cognitiva do **Google Gemini Pro**. O objetivo é fornecer não apenas a cotação, mas uma interpretação qualitativa e instantânea da volatilidade do ativo para auxiliar na tomada de decisão.

## 🚀 Funcionalidades
* **Real-time Data Fetching:** Conexão direta com a API da Binance para dados "quentes" (Preço, Variação 24h, Volume).
* **AI Analysis Engine:** Utilização de LLM (Large Language Model) para processar dados numéricos e gerar relatórios de sentimento de mercado (Bullish/Bearish).
* **Arquitetura MVC:** Backend robusto em Django separando lógica de negócios (Services) da camada de apresentação (Views).
* **Tratamento de Erros:** Resiliência caso a API externa falhe ou o ativo não exista.

## 🛠 Tech Stack
* **Backend:** Python 3.12+, Django 5.x
* **Artificial Intelligence:** Google Generative AI (Gemini 1.5 Flash)
* **Integração:** RESTful API (Binance)
* **Frontend:** Django Templates + Bootstrap 5
* **Environment Management:** Python-dotenv (Segurança de chaves)

## 🏗 Arquitetura da Solução
1.  **Input:** Usuário solicita um ativo (ex: BTCUSDT).
2.  **Service Layer:** O Django aciona o `crypto.services`.
3.  **Data Ingestion:** O sistema busca os dados brutos na Binance.
4.  **Agent Reasoning:** Os dados são injetados em um *System Prompt* otimizado no Gemini, que atua como analista financeiro.
5.  **Output:** A resposta é renderizada em HTML formatado para o usuário final.

## 📦 Como Rodar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/bv-crypto-agent.git](https://github.com/SEU-USUARIO/bv-crypto-agent.git)
   cd bv-crypto-agent
   ```

2. **Crie o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install django requests google-generativeai python-dotenv markdown
    ```

4. **Configure as Variáveis de Ambiente:**
    Crie um arquivo .env na raiz e adicione sua chave:
    ```bash
    GOOGLE_API_KEY=sua_chave_aqui
    ```

5. **Execute o servidor:**
    ```bash
    python manage.py runserver
    ```