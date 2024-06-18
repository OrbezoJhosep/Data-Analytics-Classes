import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override() #con esto estamos utilizando losz datos de yahoo finance

#Define una lista de tickets 

tickers = ["NFLX", "TSLA"]

# Importar el modulo datetime para importar fechas 

from datetime import datetime

#Define la fecha fin e inicio  usando el modulo datetime

inicio = datetime(2021,9,10)
fin = datetime(2024,6,2)


#Utiliza la función get_data_yahoo del modulo pdr para obtener los datos especificados

datos = pdr.get_data_yahoo(tickers,inicio,fin)

print(datos)