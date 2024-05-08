# 2) Faça um programa de análise de dados que leia da massa de dados de notas o filme com “ID=32” e se a nota for maior que 3 informe o nome e se é um filme bom.  

import pandas as pd

data = pd.read_csv('ratings.csv')  
filme = data[data['movieId'] == 32]

if filme['rating'].iloc[0] > 3:
    print("Filme:", filme['title'].iloc[0])
    print("E um filme bom.")
else:
    print("Filme nao encontrado")