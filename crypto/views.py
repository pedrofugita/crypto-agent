from django.shortcuts import render
from .services import get_binance_data, get_ai_analysis
import markdown

def index(request):
    # Pega o parâmetro da URL ou usa 'BTCUSDT' como padrão
    symbol = request.GET.get('symbol', 'BTCUSDT')
    
    market_data = get_binance_data(symbol)
    ai_report = None
    
    # Só chama a IA se a Binance tiver retornado dados válidos
    if 'error' not in market_data:
        raw_report = get_ai_analysis(market_data)
        # Converte o Markdown da IA para HTML
        ai_report = markdown.markdown(raw_report)
    
    context = {
        'data': market_data,
        'report': ai_report,
        'symbol': symbol
    }
    
    return render(request, 'index.html', context)