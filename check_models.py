import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERRO: Não achei a API Key. Verifique o arquivo .env")
else:
    print(f"Chave encontrada: {api_key[:5]}...*****")
    genai.configure(api_key=api_key)

    print("\n--- MODELOS DISPONÍVEIS PARA VOCÊ ---")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    except Exception as e:
        print(f"Erro ao listar modelos: {e}")