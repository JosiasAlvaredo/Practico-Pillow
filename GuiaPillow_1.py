from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")

imagen = Image.open(ruta_imagen)

imagen.show()

nombre, extension = os.path.splitext(os.path.basename(ruta_imagen))
resolucion = imagen.size
cantidad_pixeles = resolucion[0] * resolucion[1]

print("Información de la imagen:")
print("----------------------------")
print(f"| Nombre: {nombre}")
print(f"| Extensión: {extension[1:]}")
print(f"| Resolución: {resolucion[0]}x{resolucion[1]}")
print(f"| Cantidad de píxeles: {cantidad_pixeles}")
print(f"| Ubicación: {ruta_imagen}")
print("----------------------------")