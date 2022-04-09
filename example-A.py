"""
password = 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
github.com = github.githistory.xyz
pip install matplotlib
"""

# Carga de librerías
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
path_data_sales = 'https://raw.githubusercontent.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/master/data/sales_data.csv'
sales = pd.read_csv(path_data_sales, parse_dates=['Date'])

# Primeros registros de los datos
sales.head()

# Dimensión de los datos
sales.shape

# Información de las varibles
sales.info()

# Descripsión de las variables
sales.describe()

# Visualización y analisis de datos númericos
## Descripción de la variable 'Unit_Cost'
sales['Unit_Cost'].describe()

## Gráfico de cajas
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))

## Gráfico de densidad
sales['Unit_Cost'].plot(kind='density', figsize=(14,6))

## Gráfico de densidad + media + mediana
ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')

## Gráfico de histograma
ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14, 6))
ax.set_ylabel('Número de ventas')
ax.set_xlabel('Ventas')

# Visualización y analisis de datos categoricos
sales['Age_Group'].value_counts()

## Gráfico de pastel
ax = sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6, 6))

## Gráfico de barras
ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14, 6))
ax.set_ylabel('Número de ventas')

# Relación entre variables
corr = sales.corr()

## Gráfica de la relación entre variables
fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);

## Gráfico de dispersión
sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))
sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))

## Gráfico de cajas por grupos
ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')

## Gráfico de cajas por variables
boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))


cls()
