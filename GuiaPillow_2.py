from PIL import Image

ruta_imagen = "/home/jota/Escritorio/Descargas/LIMO.jpg"
image = Image.open(ruta_imagen)

image.show()

nueva_ruta = "/home/jota/Escritorio/Descargas/LIMO2.jpg"
image.save(nueva_ruta)