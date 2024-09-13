
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Function to get historical quotes
def obter_cotacoes(ticker, start, end):
    ativo = yf.Ticker(ticker)
    dados = ativo.history(start=start, end=end)
    return dados['Close']

# ETF ticker and period
ticker_hash11 = 'HASH11.SA'  # Adapte conforme necessário
ticker_defi11 = 'DEFI11.SA'  # Adapte conforme necessário
start_date = '2023-01-01'
end_date = '2024-01-01'

# Obtain historical data
cotacoes_hash11 = obter_cotacoes(ticker_hash11, start_date, end_date)
cotacoes_defi11 = obter_cotacoes(ticker_defi11, start_date, end_date)

# Align data by the index
dados = pd.DataFrame({
    'HASH11': cotacoes_hash11,
    'DEFI11': cotacoes_defi11
}).dropna()

# Correlation
correlacao = dados.corr().iloc[0, 1]
print("Correlação entre HASH11 e DEFI11:", correlacao)

# Trend line
x = dados['HASH11'].values
y = dados['DEFI11'].values

# Linear regression coefficients
coef = np.polyfit(x, y, 1)
linha_tendencia = np.poly1d(coef)

# Plot historical prices
plt.figure(figsize=(14, 7))

# Historical prices
plt.subplot(2, 1, 1)
plt.plot(dados.index, dados['HASH11'], label='HASH11', color='blue')
plt.plot(dados.index, dados['DEFI11'], label='DEFI11', color='red')
plt.title('Preços Históricos de HASH11 e DEFI11')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)

# Correl and tendence line
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

