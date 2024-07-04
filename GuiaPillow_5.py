from PIL import Image

ruta_imagen = input("Ingrese la ruta de la imagen que se desea marcar: ")

img = Image.open(ruta_imagen)
ruta_watermark = input("Ingrese la ruta de la imagen de la marca de agua: ")
watermark = Image.open(ruta_watermark)

watermark = watermark.resize((50, 50))
watermark.putalpha(int(128))

print("Seleccione la ubicación de la marca de agua:")
print("1. Superior izquierda")
print("2. Superior derecha")
print("3. Inferior izquierda")
print("4. Inferior derecha")
opcion = int(input("Ingrese la opción (1-4): "))

if opcion == 1:
    x = 50
    y = 50
elif opcion == 2:
    x = img.width - watermark.width - 50
    y = 50
elif opcion == 3:
    x = 50
    y = img.height - watermark.height - 50
elif opcion == 4:
    x = img.width - watermark.width - 50
    y = img.height - watermark.height - 50
else:
    print("Opción inválida")
    exit()

img.paste(watermark, (x, y), watermark)

imagen_watermarkeada = input("Ingrese la ruta y nombre para guardar la imagen marcada: ")
img.save(imagen_watermarkeada)

print("Imagen marcada guardada con éxito!")