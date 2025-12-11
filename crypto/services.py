import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configurações Gemini
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERRO: Chave de API não encontrada no arquivo .env")
else:
    genai.configure(api_key=api_key)

# Faz conexão com API da Binance
def get_binance_data(symbol):
    symbol = symbol.upper() # Transforma entrada do usuário em par maiúsculo ex: BTCBRL
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    
    try:
        response = requests.get(url)
        data = response.json()
    
        if 'code' in data:
            return {"error": "Moeda não encontrada. Tente BTCUSDT ou ETHUSDT."}

        return {
            "symbol": data['symbol'],
            "price": float(data['lastPrice']),
            "change_percent": float(data['priceChangePercent']),
            "volume": float(data['volume']),
            "high": float(data['highPrice']),
            "low": float(data['lowPrice']),
        }
    except Exception as e:
        return {"error": f"Erro de conexão: {str(e)}"}

def get_ai_analysis(market_data):

    # Envia os dados numéricos para o Gemini e pede uma análise qualitativa de acordo com o prompt abaixo.
    model = genai.GenerativeModel('gemini-1.5-flash') # Existem outros modelos
    
    prompt = f"""
    Você é um especialista em Criptoativos.
    Analise estes dados técnicos do {market_data['symbol']}:
    
    - Preço Atual: $ {market_data['price']:.2f}
    - Variação 24h: {market_data['change_percent']:.2f}%
    - Volume: {market_data['volume']:.2f}
    
    Responda em PORTUGUÊS com formatação Markdown:
    1. **Sentimento:** (Bullish/Bearish/Neutro)
    2. **Análise Rápida:** Explique o que a variação indica.
    3. **Recomendação Fictícia:** (Comprar/Vender/Aguardar) baseada APENAS nos dados.
    
    Seja conciso e profissional.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "A IA está indisponível no momento. Tente novamente."