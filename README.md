# 🏦 Crypto Analyst Agent (POC)

## 📌 Sobre o Projeto
Este projeto é uma **Prova de Conceito (POC)** de um Agente de IA para o mercado financeiro, desenvolvido como case prático para portfolium.

O sistema combina um **Chatbot Interativo** com um **Dashboard de Dados em Tempo Real**. Ele atua como um "Analista Junior", orquestrando dados matemáticos precisos (Binance) com a capacidade interpretativa de LLMs avançadas (Google Gemini).

## 🚀 Funcionalidades
* **Integração Híbrida:** Chatbot (Esquerda) e Dashboard Visual (Direita) na mesma interface.
* **Intent Recognition:** O sistema entende linguagem natural (ex: "Como está o Ethereum?") e busca o ativo correto.
* **Indicadores Técnicos:** Cálculo matemático próprio do **RSI (Relative Strength Index)** em tempo real.
* **AI Engine (State of the Art):** Utiliza o modelo **Google Gemini 2.5 Flash** para gerar relatórios de sentimento de mercado.
* **Compliance:** Aviso legal automático e respostas ancoradas em dados (Grounding) para evitar alucinações.

## 🛠 Tech Stack
* **Backend:** Python 3.12+, Django 5.x
* **IA:** Google Generative AI (Gemini 2.5 Flash)
* **Dados:** Binance API (REST)
* **Frontend:** HTML5, Bootstrap 5, AJAX (Fetch API)

## ⚠️ Nota sobre a API (Rate Limit)
Este projeto utiliza a versão **Gemini 2.5 Flash** (Preview), um modelo de ponta disponibilizado pelo Google.
* **Limitação:** No tier gratuito de testes, este modelo possui um limite restrito de requisições (Rate Limit).
* **Erro 429:** Caso receba uma mensagem de "Serviço indisponível", aguarde alguns minutos para a cota renovar ou altere o modelo no arquivo `services.py` para a versão `gemini-1.5-flash` (mais permissiva).

## 📦 Como Rodar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/pedrofugita/crypto-agent.git](https://github.com/pedrofugita/crypto-agent.git)
   cd crypto-agent
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
    Crie um arquivo .env na raiz do projeto e adicione sua chave do Google AI Studio:
    ```bash
    GOOGLE_API_KEY=sua_chave_aqui
    ```

5. **Execute o servidor:**
    ```bash
    python manage.py runserver
    ```

---

Desenvolvido por Pedro Fugita.