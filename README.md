# Correlation HASH11 x DEFI11

# Both are ETFs negociated in B3 the brazilian stock markets. The first is composed mainly by BITCOIN and ETHEREUM the second by protocols DEFI such UNISWAP ETHEREUM CURVE AMP and AAVE and its worth to discover the correlation of between both actives 


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para obter cotações históricas
def obter_cotacoes(ticker, start, end):
    """
    Obtém cotações históricas de um ativo usando yfinance.
    """
    ativo = yf.Ticker(ticker)
    dados = ativo.history(start=start, end=end)
    return dados['Close']

# Definir os tickers dos ETFs e o período
ticker_hash11 = 'HASH11.SA'  # Adapte conforme necessário
ticker_defi11 = 'DEFI11.SA'  # Adapte conforme necessário
start_date = '2023-01-01'
end_date = '2024-01-01'

# Obter cotações históricas
cotacoes_hash11 = obter_cotacoes(ticker_hash11, start_date, end_date)
cotacoes_defi11 = obter_cotacoes(ticker_defi11, start_date, end_date)

# Alinhar os dados pelo índice
dados = pd.DataFrame({
    'HASH11': cotacoes_hash11,
    'DEFI11': cotacoes_defi11
}).dropna()

# Calcular a correlação
correlacao = dados.corr().iloc[0, 1]
print("Correlação entre HASH11 e DEFI11:", correlacao)

# Calcular a linha de tendência
x = dados['HASH11'].values
y = dados['DEFI11'].values

# Coeficientes da regressão linear
coef = np.polyfit(x, y, 1)
linha_tendencia = np.poly1d(coef)

# Plotar os preços históricos
plt.figure(figsize=(14, 7))

# Preços históricos
plt.subplot(2, 1, 1)
plt.plot(dados.index, dados['HASH11'], label='HASH11', color='blue')
plt.plot(dados.index, dados['DEFI11'], label='DEFI11', color='red')
plt.title('Preços Históricos de HASH11 e DEFI11')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)

# Correlação com linha de tendência
plt.subplot(2, 1, 2)
plt.scatter(dados['HASH11'], dados['DEFI11'], alpha=0.5, color='green', label='Dados')
plt.plot(dados['HASH11'], linha_tendencia(dados['HASH11']), color='red', label='Linha de Tendência')
plt.title('Correlação entre HASH11 e DEFI11')
plt.xlabel('Preço HASH11')
plt.ylabel('Preço DEFI11')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

![GIThub](https://github.com/user-attachments/assets/34eb590c-7dff-4fd2-b057-a554326d38a6)


