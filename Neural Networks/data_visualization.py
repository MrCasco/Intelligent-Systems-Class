import tensorflow  as tf
import matplotlib.pyplot as plt
import flake8


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# plt.figure(figsize=(10, 5))
# i, j = 0, 0
# for p in x_train[:25]:
#     plt.subplot(5, 5, j+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(x_train[i], cmap='gray')
#     plt.xlabel("{}".format(y_train[i]))
#     j += 1
#     i += 1
# plt.show()

datos = x_train
etiquetas = y_train

##Red neuronal
modelo = tf.keras.Sequential()

#Crear las capas de la red neuronal
capa_entrada = tf.keras.layers.Flatten(input_shape=(28, 28))
modelo.add(capa_entrada)
capa_oculta = tf.keras.layers.Dense(50, activation="relu")
modelo.add(capa_oculta)
# capa_salida = tf.keras.layers.Dense(10, activation='relu')
#se usa mejor softmax que dense como salida
capa_salida = tf.keras.layers.Dense(10, activation="softmax")
modelo.add(capa_salida)

#Compilar la red neuronal
factor_aprendizaje = 0.01
# modelo.compile(optimizer=tf.train.GradientDescentOptimizer(factor_aprendizaje),loss='mse',metrics=["mse", "accuracy"])

modelo.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=["accuracy"])

#Entrenar el modelo
historia = modelo.fit(datos, etiquetas, epochs=10)

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(range(len(historia.history['accuracy'])), historia.history['accuracy'])
plt.ylabel('accuracy')
plt.xlabel('epochs')
plt.subplot(2, 2, 2)
plt.plot(range(len(historia.history['loss'])), historia.history['loss'])
plt.ylabel('loss')
plt.xlabel('epochs')
plt.show()

preddicciones = modelo.predict(x_test)
