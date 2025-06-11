import pandas as pd

df = pd.read_csv('base_vendas.csv', sep = ';')

print(df.head())

print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())


# limpeza e transformação

# converter coluna de data para datetime
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'], format='%d/%m/%Y')

# criar coluna com total da venda (valor x quant)
df['Total'] = df['Valor'] * df['Quantidade']
# verificando as primeiras linhas
print(df.head())

# conferindo os tipos das colunas
print(df.dtypes)

# ETAPA 3

import matplotlib.pyplot as plt

# 1. Soma total de vendas (coluna total q criamos)
total_vendas = df['Total'].sum()
print(f"Total de Vendas: R$ {total_vendas:.2f}")

# 2. Quantidade de vendas por categoria
vendas_por_categoria = df.groupby('Categoria')['Quantidade'].sum()
print(vendas_por_categoria)

# total de itens vendidos
total_itens = df['Quantidade'].sum()
print(f"Total de itens: {total_itens}")

# ticket médio por vendas
ticket_medio = df['Total'].mean()
print(f"Ticket médio por vendas: R$ {ticket_medio:.2f}")

# 3. Gráfico de vendas por categoria
vendas_por_categoria.plot(kind='bar', title='Quantidade vendida por categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade Vendida')
plt.show()

# Cliente que mais comprou
cliente_top = df.groupby('Cliente_ID')['Total'].sum().idxmax()
valor_top = df.groupby('Cliente_ID')['Total'].sum().max()
print(f"Cliente que mais comprou: Cliente {cliente_top} com R$ {valor_top:.2f}")


# 4. Vendas ao longo do tempo soma do mês
df['AnoMes'] = df['Data_Venda'].dt.to_period('M') # cria a coluna mes
vendas_por_mes = df.groupby('AnoMes')['Total'].sum()

vendas_por_mes.plot(kind='line', title='Total de Vendas por mes')
plt.xlabel('Ano-Mês')
plt.ylabel('Total vendas (R$)')
plt.show()