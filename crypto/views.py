from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import markdown
from .services import get_binance_data, get_ai_analysis, extract_symbol_from_text

def index(request):
    """
    Carrega a página inicial já com dados do Bitcoin para não ficar vazio.
    """
    # Estado inicial: Bitcoin
    initial_data = get_binance_data("BTCUSDT")
    
    # Se der erro no load inicial, cria um objeto vazio seguro
    if 'error' in initial_data:
        initial_data = {'symbol': 'ERRO', 'price': 0, 'change_percent': 0, 'rsi': 50}

    return render(request, 'dashboard.html', {'data': initial_data})

@csrf_exempt
def get_bot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '') # <--- A pergunta do usuário
            
            symbol = extract_symbol_from_text(user_message)
            
            if not symbol:
                return JsonResponse({
                    'response': "Não identifiquei a moeda. Tente citar o código, ex: BTC, SOL, ETH.",
                    'update_dashboard': False 
                })

            market_data = get_binance_data(symbol)
            if 'error' in market_data:
                return JsonResponse({'response': f"Erro: {market_data['error']}", 'update_dashboard': False})

            # MUDANÇA AQUI: Passamos também a user_message para a IA
            raw_analysis = get_ai_analysis(market_data, user_question=user_message)
            
            formatted_response = markdown.markdown(raw_analysis)
            
            # MUDANÇA AQUI: O Disclaimer fixo e educativo
            disclaimer = """
            <hr style="margin: 10px 0; border-top: 1px dashed #ccc;">
            <small style="color: #666; font-size: 0.85em;">
                🎓 <strong>Nota Educativa:</strong> Esta ferramenta é uma Prova de Conceito (POC). 
                Os dados são reais, mas as sugestões são geradas por IA e não constituem recomendação oficial de investimento do Banco BV. 
                Sempre faça sua própria pesquisa (DYOR).
            </small>
            """
            
            return JsonResponse({
                'response': formatted_response + disclaimer, # Junta texto + aviso
                'update_dashboard': True,
                'data': market_data
            })

        except Exception as e:
            return JsonResponse({'response': f"Erro interno: {str(e)}", 'update_dashboard': False})
            
    return JsonResponse({'error': 'Bad Request'}, status=400)