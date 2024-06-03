import cv2
# importamos las funciones necesarias para el analisis desde funciones.py
from funciones import ecualizacion_formula, mostrar_imagen_histograma, expansion_histograma

# Leer la imagen 
img = cv2.imread("pout.png")

# Verificar si la imagen es a color o en escala de grises
if len(img.shape) == 3:  # Imagen a color (3 dimensiones: R,G,B)
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:  # Imagen en escala de grises (2 dimensiones)
    img_gris = img

# Aplicar expansion del histograma a la imagen en escala de grises
img_expandida = expansion_histograma(img_gris)

# Aplicar ecualización con fórmula a la imagen en escala de grises
img_ecualizada = ecualizacion_formula(img_gris)

# Concatenar las imágenes horizontalmente
resultados_imagen = cv2.hconcat([img_gris, img_ecualizada, img_expandida])

# Mostrar imagen original en escala de grises, su ecualización y su expansion
cv2.imwrite('image/resultados.jpeg', resultados_imagen)

# Mostrar histogramas
mostrar_imagen_histograma(img_gris, img_ecualizada, img_expandida)

cv2.waitKey(0)
cv2.destroyAllWindows()
