# Open In Colab

# Importação
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report ,ConfusionMatrixDisplay


# Tabela de idade , altura, peso, salario, faculdade, nome, time
df= pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/nba.csv')
df

df['Age'] = df['Age'] + df['Weight'] + 1

df.drop(columns='Salary')


df.dropna(subset='Height', inplace=True)
df.dropna(subset='Weight', inplace=True)

df = df.drop_duplicates()


def convertWeight(x):
    return x * 0.453592


texto = '175 cm'
lista = texto.split()
lista

['175', 'cm']


def convertHeight(x):
    foot = int(x.split('-')[0])
    inch = int(x.split('-')[1])
    return (foot * 12 + inch) * 0.0254  # convertido tudo para metro


# def arvore():


# compreensão
df['Weight(kg)'] = [convertWeight(x) for x in df['Weight']]
df['Height(m)'] = [convertHeight(x) for x in df['Height']]

colunas = ['Name', 'Team', 'Position', 'Age', 'Height(m)', 'Weight(kg)', 'College', 'Salary']
df = df[colunas]

df

grupos = df.groupby(by='Position')
grupos.first()

grupos.get_group('SF')['Age'].mean()


np.float64(249.63529411764705)


# Grupos
# grupos.get_group('Boston Celtics')['Age'].median()
# grupos.get_group('Boston Celtics')['Age'].mean()
grupos.get_group('SG')['Age'].mean()



np.float64(234.22549019607843)


df.columns


Index(['Name', 'Team', 'Position', 'Age', 'Height(m)', 'Weight(kg)', 'College',
       'Salary'],
      dtype='object')


df.info()

df.describe()


GroupBy = df.groupby(by='Salary')
GroupBy.first()


f1 = f1_score(y_test, y_pred, average='weighted')
acuracia = accuracy_score(y_test, y_pred)
reporta = classification_report(y_test, y_pred)

print(f"Relatório:\n{reporta}")
print(f"Acurácia: {acuracia}")
print(f"F1 Score: {f1}")



