import cv2
from funciones import howis, ecualizacion_formula, mostrar_imagen_histograma

# Leer la imagen 
img = cv2.imread("pout.png")

# Verificar si la imagen es a color o en escala de grises
if len(img.shape) == 3:  # Imagen a color (3 dimensiones: R,G,B)
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:  # Imagen en escala de grises (2 dimensiones)
    img_gris = img

# Mostrar información de la imagen original en color y en escala de grises
howis(img)
howis(img_gris)

# Aplicar ecualización con fórmula a la imagen en escala de grises
img_ecualizada = ecualizacion_formula(img_gris)

# Mostrar imagen original en escala de grises y su ecualización
cv2.imshow('Imagen real e Imagen ecualizada', cv2.hconcat([img_gris, img_ecualizada]))

# Mostrar histogramas
mostrar_imagen_histograma(img_gris, img_ecualizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
