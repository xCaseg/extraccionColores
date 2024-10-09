import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

# Paso 1: Importar una imagen con la librería cv2 
ruta = r'C:\Users\DELL\Desktop\Imagen.jpg'
imagen = cv2.imread(ruta)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Paso 2: Convertir la imagen a un array
Matriz1 = np.asarray(imagen_rgb)

# Paso 3: Detectar el formato del color
def detectar_formato(imagen):
    if len(imagen.shape) == 2:
        return "Escala de grises (PGB)"
    elif len(imagen.shape) == 3:
        if imagen.shape[2] == 3:
            return "RGB"
        elif imagen.shape[2] == 4:
            if (imagen[:, :, 3] == 255).all():
                return "RGBA"
            else:
                return "RGBA (con transparencia)"
    else:
        return "Formato de color no reconocido"

formato = detectar_formato(Matriz1)
print("El formato de color de la imagen es:", formato)

# Paso 4: Determinar las dimensiones de la imagen
alto, ancho, profundidad = Matriz1.shape
print("Altura de la imagen:", alto)
print("Anchura de la imagen:", ancho)
print("Profundidad de la imagen (número de canales de color):", profundidad)
print("Cantidad de pixeles:", Matriz1.size)

# Paso 5: Seleccionar dos píxeles de muestra
x1, y1 = 187, 62
muestra1 = Matriz1[x1, y1]
print(f"Se ha seleccionado el píxel 1 de las coordenadas ({x1}, {y1})")
print("Valor del píxel 1 RGB:", muestra1)

x2, y2 = 460, 224
muestra2 = Matriz1[x2, y2]
print(f"Se ha seleccionado el píxel 2 de las coordenadas ({x2}, {y2})")
print("Valor del píxel 2 RGB:", muestra2)

# Paso 6: Crear una nueva matriz con las mismas dimensiones que Matriz1
Matriz2 = np.empty((alto, ancho, profundidad), dtype=np.uint8) 

# Paso 7: Calcular la distancia euclidiana entre los píxeles de muestra
d_rango = math.sqrt((muestra1[0] - muestra2[0])**2 + (muestra1[1] - muestra2[1])**2 + (muestra1[2] - muestra2[2])**2) 
#Se usa para determinar si los píxeles de la imagen original están dentro del rango establecido.

# Paso 8: Comparar y asignar los píxeles a la nueva matriz

# Se recorrerán los píxeles de la imagen original utilizando dos bucles for. Para cada píxel de la imagen original, se calcula la distancia euclidiana entre ese píxel 
# y el píxel de muestra (muestra1). 
# Luego, se compara esta distancia con el rango (d_rango) establecido en el paso anterior.

for i in range(alto):
    for j in range(ancho):
        # Calcular la distancia euclidiana entre el píxel actual de la imagen original y el píxel de muestra
        distancia_entre_pixel_y_muestra = math.sqrt((Matriz1[i, j][0] - muestra1[0])**2 + (Matriz1[i, j][1] - muestra1[1])**2 + (Matriz1[i, j][2] - muestra1[2])**2)
        # Verificar si la distancia entre el píxel actual y el píxel de muestra está dentro del rango establecido
        if distancia_entre_pixel_y_muestra < d_rango:
            # Si el píxel actual está dentro del rango, copiarlo a la nueva matriz
            # Si la distancia euclidiana entre el píxel de la imagen original y el píxel de muestra es menor que el rango establecido (d_rango), se asigna el valor del píxel de la imagen original a la Matriz2. 
            Matriz2[i, j] = Matriz1[i, j]
        else:
            # Si el píxel actual está fuera del rango, asignar el color blanco
            Matriz2[i, j] = [255, 255, 255]


# Paso 9: Imprimir Matrices
plt.imshow(Matriz1)
plt.title("Matriz 1")
plt.show()

# Mostrar la matriz resultante
plt.imshow(Matriz2)
plt.title('Matriz 2')
plt.show()