# 🛠️ Script de Automação de Infraestrutura (IT Support Automation)

## 🎯 Objetivo do Projeto
Demonstrar a aplicação de scripting Python para automatizar tarefas críticas de rotina no Suporte Técnico e Monitoramento de Infraestrutura. O foco é otimizar o tempo de diagnóstico e reduzir a intervenção manual.

## ⚙️ Solução e Funcionalidades
Este script foi desenvolvido para monitorar o status de múltiplos serviços web críticos simultaneamente (como Google, Microsoft e GitHub), o que é essencial para um ambiente de suporte N2/Infra.
- **Diagnóstico:** Envia requisições HTTP para verificar o código de status de forma não-invasiva.
- **Status:** Retorna 'ONLINE' para sucesso (código 200).
- **Alerta:** Retorna 'FALHA CRÍTICA' para erros de conexão ou *timeouts*, permitindo ação imediata.

## 🐍 Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Bibliotecas:** `requests` (para requisições HTTP), `datetime`
- **Controle de Versão:** Git / GitHub

## 💻 Como Executar (Instruções)
1. Certifique-se de que a biblioteca `requests` está instalada (`pip install requests` ou `conda install requests`).
2. Execute o script no terminal:
```bash
python monitor_status.py
