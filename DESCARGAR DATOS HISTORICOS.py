import os
import yfinance as yf
import pandas as pd

# Lista de acciones
stocks = ['^SPX','^IXIC','^MXX','^STOXX','^GDAXI','^FCHI','^VIX',
            'XLK','XLF','XLV','XLE','XLC','XLY','XLP','XLI','XLB','XLRE','XLU',
            'SPY','EWW',
            'IVW','IVE','QUAL','MTUM','SIZE','USMV',
            'AAPL','MSFT','NVDA','AMZN','GOOG','META','NFLX',
            'BRK-B','JPM','V','MA','BAC','MS','GS','BLK',
            'LLY','JNJ','PG','MRK','ABBV','PFE',
            'BTC-USD','ETH-USD','SOL-USD','USDC-USD','USDT-USD','DAI-USD',
            'EURUSD=X','GBPUSD=X','CHFUSD=X','SEKUSD=X','NOKUSD=X','JPYUSD=X','MXNUSD=X',"GGAL.BA","YPFD.BA","BMA.BA","PAMP.BA","TECO2.BA","SUPV.BA", "CEPU.BA", "COME.BA","TXAR.BA", "ALUA.BA","EDN.BA","TGSU2.BA","MIRG.BA", "TRAN.BA","CRES.BA", "HARG.BA","IRSA.BA","LOMA.BA","VALO.BA","AGRO.BA"]

# Crear una carpeta si no existe
if not os.path.exists("data-master"):
    os.makedirs("data-master")

# Definir la fecha de inicio
start_date = '2024-01-01'  # Fecha de inicio
end_date = '2024-12-17'

# Descargar datos históricos y guardarlos en archivos CSV
for stock in stocks:
    ticker = yf.Ticker(stock)  # ".BA" es el sufijo para acciones de la BCBA
    data = ticker.history(start=start_date,end=end_date, interval="1d")
    data.to_csv(f"data-master/{stock}.csv")



