import pandas as pd

df = pd.read_csv('data.csv')
print("\n")

print(df)
print(df.sort_values(by=["Duration", "Calories"], ascending=False, inplace=False, ignore_index=True))
print("\n")

# Head and tail
print(df.head(3))
print(df.tail(5))
print("\n")

print(df.dropna(axis=0, how='any', inplace=True))
print(df)

print("\n")

df.loc[7, 'Duration'] = 45
df.loc[26, 'Date'] = "2020/12/26"

# Removendo colunas (características)
colunas = ['Duration', 'Pulse', 'Maxpulse', 'Calories']

df = df[colunas]

print(df)
print("\n")

# Removendo colunas (características)
colunas = ['Duration', 'Pulse', 'Maxpulse', 'Calories']
print("\n")

df = df[colunas]
print(df)
print("\n")

# Correlação de variáveis (características)
print(df.corr())
print("\n")

# Shape (linhas, colunas)
df.shape
print("\n")

# Columns (colunas)
df.columns
print("\n")

# Info
df.info()
print("\n")

# Describe
df.describe()
print("\n")
# Value Counts
df.value_counts()
print("\n")

# Medidas estatísticas
df['Calories'].mean()