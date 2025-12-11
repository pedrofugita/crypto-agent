# crypto/services.py
import requests
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

def calculate_rsi(prices, period=14):
    """Calcula o RSI matematicamente."""
    if len(prices) < period + 1:
        return 50 
    gains = []
    losses = []
    for i in range(1, len(prices)):
        delta = prices[i] - prices[i-1]
        if delta > 0:
            gains.append(delta)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(delta))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0: return 100
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def extract_symbol_from_text(text):
    """Extrai o símbolo da criptomoeda do texto do usuário."""
    text = text.upper()
    mapping = {
        "BITCOIN": "BTCUSDT", "BTC": "BTCUSDT",
        "ETHER": "ETHUSDT", "ETHEREUM": "ETHUSDT", "ETH": "ETHUSDT",
        "SOLANA": "SOLUSDT", "SOL": "SOLUSDT",
        "DOGE": "DOGEUSDT", "PEPE": "PEPEUSDT",
        "XRP": "XRPUSDT", "RIPPLE": "XRPUSDT"
    }
    for key, value in mapping.items():
        if key in text: return value
    match = re.search(r'([A-Z]{3,5}USDT)', text)
    if match: return match.group(1)
    return None

def get_binance_data(symbol):
    """Busca dados na Binance."""
    symbol = symbol.upper()
    try:
        # Dados atuais
        url_ticker = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        resp_ticker = requests.get(url_ticker)
        data = resp_ticker.json()
        if 'code' in data: return {"error": "Moeda não encontrada."}

        # Histórico para RSI
        url_klines = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=20"
        resp_klines = requests.get(url_klines).json()
        closing_prices = [float(candle[4]) for candle in resp_klines]
        rsi_value = calculate_rsi(closing_prices)

        return {
            "symbol": data['symbol'],
            "price": float(data['lastPrice']),
            "change_percent": float(data['priceChangePercent']),
            "volume": float(data['volume']),
            "high": float(data['highPrice']),
            "low": float(data['lowPrice']),
            "rsi": rsi_value,
        }
    except Exception as e:
        return {"error": f"Erro Binance: {str(e)}"}

def get_ai_analysis(market_data, user_question=""):
    """
    Gera análise usando Gemini 2.5 Flash.
    """

    model = genai.GenerativeModel('models/gemini-2.5-flash') 
    
    prompt = f"""
    Atue como um Consultor de Investimentos do Banco BV (High Frequency Trading).
    
    PERGUNTA DO USUÁRIO: "{user_question}"
    
    DADOS TÉCNICOS ({market_data['symbol']}):
    - Preço: $ {market_data['price']}
    - Variação 24h: {market_data['change_percent']}%
    - RSI (14h): {market_data['rsi']}
    
    Responda em Markdown (PT-BR). Seja direto:
    **Análise Técnica:** (Interprete o RSI e a tendência)
    **Conclusão:** (Responda DIRETAMENTE à pergunta do usuário. Use linguagem profissional de banco.)
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"🔴 ERRO TÉCNICO GEMINI: {e}")
        return "Serviço de IA indisponível momentaneamente. Verifique os dados no painel."