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

#Calcular el promedio, la desviación estandar valores minimos y maximos, para ello usamos el modulo describe()

#print(matrizPrecios.describe())

"""
Count : Para todos los tickets hay 1259  datos disponibles
mean: Precio promedio específico para cada ticker 185.3364 para Tesla por ejemplo
std: Desviación standar, dispersión de los datos ajustados. Para Tesla indica que tiene una alta variabilidad
min: Valor minimo de los precios ajustados, para coca cola es 46.52
25%: el 25% de los datos estan por debajo del valor 111 para apple
50%: el 50% de los datos están por debajo del valor 203 para testla
max: el valor máximo
 
"""

#Esta línea importa el módulo pyplot de matplotlib, una biblioteca de Python utilizada para crear gráficos y visualizaciones.
import matplotlib.pyplot as plt

import seaborn as sns

# Crear un DataFrame con los datos de AAPL y MSFT
data_comparacion = matrizPrecios[['AAPL', 'MSFT']]

# Creamos un gráfico de dispersión (scatter plot) para ver la relación entre ambos precios
plt.figure(figsize=(10,6))
sns.scatterplot(x='AAPL', y='MSFT', data=data_comparacion)

# Títulos y etiquetas
plt.title('Relación entre Precios Ajustados de AAPL y MSFT')
plt.xlabel('Precio Ajustado AAPL')
plt.ylabel('Precio Ajustado MSFT')

# Mostrar el gráfico
plt.show()


# Crear un histograma para la distribución de precios de TSLA
plt.figure(figsize=(10,6))
sns.histplot(matrizPrecios['TSLA'], bins=30, kde=True)

# Títulos y etiquetas
plt.title('Distribución de Precios Ajustados de Tesla (TSLA)')
plt.xlabel('Precio Ajustado TSLA')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()
