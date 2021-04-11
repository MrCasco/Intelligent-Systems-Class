import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OrdinalEncoder, OneHotEncoder
import matplotlib.pyplot as plt

datos = pd.read_csv("prep/housing.csv")

#scatter_matrix(datos)
#plt.show()

# FASE 1: Separar datos en entrenamiento y pruebas
datos, validacion = train_test_split(datos, test_size=0.2, random_state=13)
# datos tiene 16512 renglones

# print(datos.shape)
# print(validacion.shape)

# FASE 2: Limpieza de datos - Algoritmos necesitan datos completos
# 1. Borrar renglones vacíos
# datos = datos.dropna(subset=["total_bedrooms"])

# 2. Borrar la columna
# datos = datos.drop("total_bedrooms", axis=1)

# 3. Rellenar con algún valor
valor_medio = datos["total_bedrooms"].median()
datos["total_bedrooms"].fillna(valor_medio, inplace=True)

# FASE 3: Escalamiento de datos - Algoritmos son sensibles a diferentes rangos de valores
# 1. Normalización (Rango de valores está entre 0 y 1) Se ve afectada por intrusos
# datos2 = datos.drop("ocean_proximity", axis=1)
# scaler = MinMaxScaler()
# resultado = scaler.fit_transform(datos2)
# datos_normalizados = pd.DataFrame(resultado, columns=datos2.columns, index=datos2.index)
# datos_normalizados["ocean_proximity"] = datos["ocean_proximity"]
# print(datos_normalizados.describe())

# 2. Estandarización (El promedio es 0 y la desv. estandar es 1)
datos2 = datos.drop("ocean_proximity", axis=1)
scaler = StandardScaler()
resultado = scaler.fit_transform(datos2)
datos_normalizados = pd.DataFrame(resultado, columns=datos2.columns, index=datos2.index)
datos_normalizados["ocean_proximity"] = datos["ocean_proximity"]
#print(datos_normalizados.describe())

# FASE 4: Convertir categorías a valores numéricos - Algoritmos trabajan solo con números
# print(datos_normalizados["ocean_proximity"].value_counts())

# 1. Codificación ordinal (1 número secuencial a cada valor)
# encoder = OrdinalEncoder()
# resultado = encoder.fit_transform(datos_normalizados[["ocean_proximity"]])

# 2. Codificación OneHot (1 columna con valores binarios (0/1) por cada categoría
encoder = OneHotEncoder()
resultado = encoder.fit_transform(datos_normalizados[["ocean_proximity"]])


