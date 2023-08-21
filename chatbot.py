import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import os
import pyfiglet
from colorama import Fore, Back, Style
import time
import sys
import re

# Configurar el stemmer
stemmer = LancasterStemmer()

# Cargar los datos de entrenamiento desde el archivo intents.json
with open('intents.json') as file:
    data = json.load(file)

# Obtener los patrones, las etiquetas y las respuestas de los datos
patterns = []
labels = []
responses = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenizar y stemizar el patrón
        words = nltk.word_tokenize(pattern)
        words = [stemmer.stem(word.lower()) for word in words]
        patterns.append(words)
        labels.append(intent['tag'])
        responses.append(intent['responses'])

# Declarar una lista para almacenar el historial de conversación
conversation_history = []

# Crear un diccionario de palabras únicas
words = []
for pattern in patterns:
    words.extend(pattern)
words = sorted(list(set(words)))

# Crear conjuntos de entrenamiento y salida
training = []
output = []
output_empty = [0] * len(labels)

for idx, pattern in enumerate(patterns):
    bag = []
    # Crear una bolsa de palabras de 1s y 0s para cada patrón
    for word in words:
        bag.append(1) if word in pattern else bag.append(0)
    # Crear la salida correspondiente a la etiqueta
    output_row = list(output_empty)
    output_row[labels.index(labels[idx])] = 1
    # Agregar el patrón y la salida a los conjuntos de entrenamiento y salida
    training.append(bag)
    output.append(output_row)

# Convertir los conjuntos de entrenamiento y salida a arreglos numpy
training = np.array(training)
output = np.array(output)

# Restablecer el grafo predeterminado de TensorFlow
tf.compat.v1.reset_default_graph()

# Definir los hiperparámetros
learning_rate = 0.001
batch_size = 64
num_epochs = 2000

# Construir la red neuronal
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 1
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 2
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 3
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 4
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 5
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 6
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 7
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 8
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 9
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 10
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 11
net = tflearn.fully_connected(net, 200, activation='relu')
net = tflearn.dropout(net, keep_prob=0.5)  # Capa de dropout 12
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net, learning_rate=learning_rate)

# Definir el modelo y cargar el modelo guardado si existe
model = tflearn.DNN(net)
model_file = 'model.tflearn'
if os.path.isfile(model_file):
    model.load(model_file)
else:
    # Entrenar el modelo si no hay un modelo guardado
    model.fit(training, output, n_epoch=num_epochs, batch_size=batch_size, show_metric=True, 
              snapshot_epoch=True, snapshot_step=500)  # Aumentar el número de épocas y agregar puntos de control
    model.save(model_file)


def normalize_user_input(user_input):
    # Convertir todo a minúsculas
    normalized_input = user_input.lower()

    # Remover caracteres especiales y puntuación
    normalized_input = re.sub(r"[^\w\s]", "", normalized_input)

    # Remover espacios adicionales
    normalized_input = re.sub(r"\s+", " ", normalized_input).strip()

    return normalized_input

    # Función para procesar la entrada
def get_response(user_input):
    # Normalizar la pregunta del usuario
    normalized_input = normalize_user_input(user_input)

    # Tokenizar y stemizar la pregunta normalizada del usuario
    user_words = nltk.word_tokenize(normalized_input)
    user_words = [stemmer.stem(word.lower()) for word in user_words]
    user_bag = [0] * len(words)
    for user_word in user_words:
        if user_word in words:
            user_bag[words.index(user_word)] = 1

    # Predecir la etiqueta de la pregunta del usuario normalizada
    results = model.predict([np.array(user_bag)])
    results_index = np.argmax(results)
    tag = labels[results_index]

    if results[0][results_index] < 0.5:
        response = "Por favor, reformula tu pregunta de una forma más detallada."
    else:
        response = random.choice(responses[results_index])

    return response


# Función para imprimir el banner
def print_banner():
    banner_text = pyfiglet.figlet_format("Yarvis AI", font="standard")
    colored_banner = Fore.YELLOW + banner_text + Style.RESET_ALL
    print(Back.BLUE + colored_banner + Style.RESET_ALL)

# Función principal del chatbot
def chat():
    # Imprimir el banner
    print_banner()

    # Saludo inicial
    print("YARVIS: ¡Hola! ¿En qué puedo ayudarte hoy?")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "goodbye":
            print(Fore.RED + "YARVIS: ¡Adiós! ¡Que tengas un gran día!" + Style.RESET_ALL)
            break
        else:
            response = get_response(user_input)
            print(Fore.GREEN + "YARVIS:", end=Style.RESET_ALL)
            sys.stdout.flush()  # Asegurar que el mensaje del chatbot se muestre de inmediato

            for char in response:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)  # Retraso entre caracteres para simular la escritura en tiempo real

            print()  # Salto de línea después de que se completa la respuesta del chatbot

# Ejecutar el chatbot
chat()