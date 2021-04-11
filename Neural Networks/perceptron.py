import tensorflow as tf
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

modelo = tf.keras.Sequential()

capa_entradas = 
