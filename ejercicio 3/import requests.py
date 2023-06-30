import requests

url = "https://media.istockphoto.com/id/1389401258/es/foto/perrito.jpg?s=1024x1024&w=is&k=20&c=7RIsD2HLxbd80zVGtGRBrKhLtBXEjPP5YQMwKa6QjPw="  # Reemplaza con la URL de la imagen que deseas descargar
perrito = "imagen_descargada.jpg"  # Nombre del archivo de destino

response = requests.get(url)
response.raise_for_status()  # Verifica si la respuesta tiene algún error

with open(perrito, "wb") as file:
    file.write(response.content)

print("La imagen se ha descargado exitosamente.")