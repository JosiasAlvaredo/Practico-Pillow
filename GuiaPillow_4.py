import os
from PIL import Image

if not os.path.exists("recortes"):
    os.makedirs("recortes")

contador_recortes = 0

while True:
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    if not os.path.exists(ruta_imagen):
        print("La imagen no existe")
        continue

    img = Image.open(ruta_imagen)

    x_inicio = int(input("Ingrese la coordenada x inicial: "))
    y_inicio = int(input("Ingrese la coordenada y inicial: "))

    ancho_recorte = int(input("Ingrese el ancho del recorte: "))
    alto_recorte = int(input("Ingrese el alto del recorte: "))

    if x_inicio + ancho_recorte > img.width or y_inicio + alto_recorte > img.height:
        print("El recorte excede los límites de la imagen")
        continue

    recorte = img.crop((x_inicio, y_inicio, x_inicio + ancho_recorte, y_inicio + alto_recorte))

    contador_recortes += 1
    nombre_recorte = f"recortes/recorte{contador_recortes}.png"
    recorte.save(nombre_recorte)

    print(f"Recorte guardado en {nombre_recorte}")