# 1) Ler a massa de dados de notas, mostrar os 12 primeiros registros, os 6 últimos registros e o tamanho total da massa de dados.

import pandas as pd

data = pd.read_csv('movie.csv')

print("Os 12 primeiros :")
print(data.head(12))
print("Os 6 ultimos : ") 
print(data.tail(6))
print("Tamanho total de dados:")
print(data.size)