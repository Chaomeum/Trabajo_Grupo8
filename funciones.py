import numpy as np
import matplotlib.pyplot as plt

def howis(img):
    print('size = ', img.shape)
    print('max  = ', np.max(img))
    print('min  = ', np.min(img))

def calcular_histograma(img):
    # Obtenemos las dimensiones de la imagen
    width, height = img.shape
    # Inicializa un array de ceros para almacenar el histograma
    y = np.zeros(256)
    
    #se incrementa el recuento correspondiente a cada valor de intensidad encontrado en la imagen
    for w in range(width):
        for h in range(height):
            # Se obtiene el valor del pixel actual
            v = img[w, h]
            # Incrementa el conteo en el histograma para el valor de intensidad actual
            y[v] = y[v] + 1
    # se retorna el histograma
    return y

def ecualizacion_formula(img):
    # la tupla almacena los datos correspodientes a la imagen
    width, height = img.shape
    # Calcula el histograma de la imagen utilizando la función calcular_histograma
    y = calcular_histograma(img)
    # Crea una matriz de ceros del mismo tamaño que la imagen original
    img_ecualizada = np.zeros((width, height), img.dtype)

    # Determina el factor de escala k
    k = 255 / (width * height)  # En la formula equivale a (L-1)/MN
    suma = 0 # acumulador de la sumatoria de frecuencias
    
    # Recorre la imagen pixel por pixel
    for w in range(width):
        for h in range(height):
            # Realiza la sumatoria acumulada de las frecuencias hasta el valor del píxel actual
            for s in range(img[w, h]):
                suma += y[s]
            # Asigna el nuevo valor al píxel ecualizado utilizando la fórmula de ecualización
            img_ecualizada[w, h] = k * suma
            # Se reinicia el contador por cada pixel analizado
            suma = 0
    # Retorna la imagen ecualizada
    return img_ecualizada

def mostrar_imagen_histograma(img_original, img_ecualizada):
    # Obtiene las dimensiones de la imagen original
    width, height = img_original.shape
    # Genera una secuencia de valores de intensidad de píxeles de 0 a 255
    x = np.linspace(0, 255, num=256, dtype=np.uint8)
    
    # Calcula los histogramas de la imagen original y la imagen ecualizada
    y_original = calcular_histograma(img_original)
    y_ecualizada = calcular_histograma(img_ecualizada)
    
    # Crea una figura con dos subtramas (una para cada histograma)
    plt.figure(figsize=(10, 6))

    # Subtrama para el histograma  de la imagen original
    plt.subplot(1, 2, 1), plt.bar(x, y_original)
    # Subtrama para el histograma de la imagen ecualizada
    plt.subplot(1, 2, 2), plt.bar(x, y_ecualizada)
    # Realiza comparativa entre los dos histogramas
    plt.show()
