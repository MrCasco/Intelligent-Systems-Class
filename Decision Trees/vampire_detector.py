from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("vampires.csv")

caracteristicas = pd.get_dummies(datos[["shadow", "garlic", "skin", "accent"]], drop_first=True)
etiquetas = pd.get_dummies(datos[["vampire"]], drop_first=True)

arbol = tree.DecisionTreeClassifier(criterion='entropy')
resultado = arbol.fit(caracteristicas, etiquetas)
tree.plot_tree(resultado, feature_names=caracteristicas.columns)
plt.show()
