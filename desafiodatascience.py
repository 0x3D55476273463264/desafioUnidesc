# Análise de Dados com Python pode ajudar as organizações a entender seus dados com mais rapidez, usando Python para identificar padroes nos dados e melhorar os resultados de negocio. A analitica de Dados com python pode ser usada por analistas de dados na exploracao de dados para escrever scripts e funcoes customizadas, manipular os dados, otimizar fluxo de trabalho e gerar visualizações de dados.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("case-brazil-cities.csv")  

# 1. Cidade com mais casos de COVID
cidadeMais = data[data['totalCases'] == data['totalCases'].max()]

# 2. Cidade com menos casos de COVID
cidadeMenos = data[data['totalCases'] == data['totalCases'].min()]

# 3. Estado com mais casos de COVID
estadoMais = data.groupby('state')['totalCases'].sum().idxmax()

# 4. Estado com menos casos de COVID
estadoMenos = data.groupby('state')['totalCases'].sum().idxmin()

# 5. Cidade com mais mortes por COVID
cidadeMaisMortes = data[data['deaths'] == data['deaths'].max()]

# 6. Cidade com menos mortes por COVID
cidadeMenosMortes = data[data['deaths'] == data['deaths'].min()]

# 7. Estado com mais mortes por COVID
estadoMaisMortes = data.groupby('state')['deaths'].sum().idxmax()

# 8. Estado com menos mortes por COVID
estadoMenosMortes = data.groupby('state')['deaths'].sum().idxmin()

# 9. Total de casos de COVID no Brasil
totalCasos = data['totalCases'].sum()

# 10. Total de mortes por COVID no Brasil
totalMortes = data['deaths'].sum()

# 11. Gráfico com 5 estados com mais mortes
topEstadosMortes = data.groupby('state')['deaths'].sum().nlargest(5)
topEstadosMortes.plot(kind='bar')
plt.title('5 Estados com Mais Mortes por COVID')
plt.ylabel('Mortes')
plt.xlabel('Estado')
plt.show()

# 12. Histograma com 5 estados com menos mortes
estadosMortes = data.groupby('state')['deaths'].sum().nsmallest(5)
estadosMortes.plot(kind='hist', bins=5)
plt.title('Distribuição das Mortes nos 5 Estados com Menos Mortes')
plt.ylabel('Numero de Estados')
plt.xlabel('Mortes')
plt.show()
