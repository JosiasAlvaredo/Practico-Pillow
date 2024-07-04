from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")
angulo_rotacion = int(input("Ingrese el ángulo de rotación: "))

imagen = Image.open(ruta_imagen)

imagen_rotada = imagen.rotate(angulo_rotacion)

imagen_rotada.show()

nombre_archivo, extension = os.path.splitext(ruta_imagen)
nombre_archivo_rotada = f"{nombre_archivo}Rot{extension}"
imagen_rotada.save(nombre_archivo_rotada)

print(f"Imagen guardada como {nombre_archivo_rotada}")