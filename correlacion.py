#Importamos la librería numpy ya que brinda soporte para arrays, matrices grandes y mutidimensional 
#Además nos brinda una serie de funciones matematicas para operar con estos arrays
import numpy as np

#Pandas es una biblioteca de manipulación y analisis de datos que nos permite trabajar con estructura de datos como
# DataFrames que nos ayuda a almacenar y manipular datos
import pandas as pd 

#Yfinance es una biblioteca  que facilita la obtención de los datos financieros históricos y actuales
import yfinance as yf

#Pandas datereader es una extensión de pandas que permite leer datos directamente desde diversas fuentes como yahoo fiannce
from pandas_datareader import data as pdr

#Datetime es un modulo estandar de python que suministra y manipula fechas y horas
from datetime import datetime


#funcion para extraer los datos directamente de yahoo finance
yf.pdr_override()


#Las empresas de las cuales vamos a sacar la información de yahoo finance
listatickers = ['TSLA', 'AAPL', 'KO', 'MCD', 'NFLX', 'WMT', 'F', 'EBAY', 'AMZN', 'MSFT']

#Fecha para extraer los datos
inicio = datetime(2019,6,8)
fin = datetime(2024,6,8)

#Crear un Dataframe vacío de pandas llamado matrices para almacenar la información
matrizPrecios = pd.DataFrame()

#Finalmente hacemos un bucle for para obtener los datos de la lista de tickers del precio ajustado
for t in listatickers:
    matrizPrecios[t] = pdr.get_data_yahoo(t,inicio,fin)['Adj Close']
    
# Calcular la correlación
correlacion = matrizPrecios.corr()
print(correlacion)
