import requests
import datetime
import sys

# LISTA DE ENDEREÇOS DE SERVIÇOS WEB
LISTA_URLS = [
    "https://www.google.com", 
    "https://www.microsoft.com", 
    "https://github.com"
]

# Funcao de monitoramento de status
def checar_status_servico(url):
    try:
        
        if 'requests' not in sys.modules:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] - Aviso: Tentando instalar a biblioteca 'requests'...")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            global requests
            import requests 
        
        # Envia uma requisicao GET e espera 5 segundos por uma resposta
        resposta = requests.get(url, timeout=5)
        
        # O status code 200 significa sucesso
        if resposta.status_code == 200:
            status = "ONLINE"
        else:
            status = f"ALERTA! Código de Status: {resposta.status_code}"
            
    except requests.exceptions.RequestException as e:
        # Captura erros de conexao (servico fora do ar, DNS falhou)
        status = f"FALHA CRÍTICA! Erro: {e}"
        
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - Status do Serviço ({url}): {status}")


if __name__ == "__main__":
    print("--- INICIANDO MONITORAMENTO DE SERVIÇOS DE INFRA ---")
    
    # Loop para checar cada URL na lista
    for url in LISTA_URLS:
        checar_status_servico(url)
        
    print("--- MONITORAMENTO CONCLUÍDO ---")