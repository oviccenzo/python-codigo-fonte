import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("src/dataset_alunos_universitarios.csv")

print("\n")

print("A primeira linha do dataset: ")
print(df.head())

print("\n")

print("\nInfromção do dataset: ")
print(df.info())

print("\n")

# 2 Pré processamento
#Converter variáveis categóricas para numéricas
le_dict = {}

for col in df.select_dtypes(include='object').columns:
  le = LabelEncoder()
  df[col] = le.fit_transform(df[col])
  le_dict[col] = le

print("\n")

X = df.drop("status_curso",axis=1)
y = df["status_curso"]
print("\nFeatures: ")
print(X.columns)

print("\n")
X_train , X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\n")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

print(model.fit(X_train, y_train))

print("\n")

y_pred = model.predict(X_test)
print("\nRelatorios de classificacao: ")
print(classification_report(y_test,y_pred))

print("\n")

importances = model.feature_importances_
features_importance = pd.DataFrame({
    "feature":X.columns,
    "importance":importances
})

features_importance = features_importance.sort_values(
    by="importance",
    ascending=False
)

print("\n")

print(f"Feature importances")
print(features_importance)

print("\n")

plt.figure()
plt.barh(features_importance["feature"], features_importance["importance"])
plt.gca().invert_yaxis()
plt.title("Feature importances")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()

#Sha
# Criar o explainer
explainer = shap.TreeExplainer(model, X_train)
#Calcular os valores do shap
shap_values = explainer(X_test, check_additivity=False)
#Selecionar uma classes (evadiu ou concluiu)
shap_class = shap_values.values[:,:,1]

shap.summary_plot(
    shap_class,
    X_test,
    feature_names = X_test.columns
)

#Explicação de um previsão individual do dataset da evasão de aluno
index = 10
shap.plots.waterfall(
    shap.Explanation(
        values = shap_class[index],
        base_values = explainer.expected_value[1],
        data = X_test.iloc[index],
        feature_names = X_test.columns
    )
)

print("\n")

index = 10
sample = X_test.iloc[[index]]
prediction = model.predict(sample)[0]
prob = model.predict_proba(sample)[0]

print(f"Previsão: {prediction}")
print(f"Probabilidade: {prob}")

print(f"Valores de amostras: {sample}")