import random
from pyfiglet import Figlet

# Obtener la lista de fuentes disponibles
figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

# Solicitar al usuario el nombre de la fuente
fuente_seleccionada = input("Ingresa el nombre de la fuente (deja vacío para seleccionar una aleatoria): ")
if not fuente_seleccionada:
    # Seleccionar una fuente aleatoria si no se ingresó ninguna
    fuente_seleccionada = random.choice(fuentes_disponibles)

# Solicitar al usuario el texto a imprimir
texto_imprimir = input("Ingresa el texto a imprimir: ")

# Configurar la fuente seleccionada
figlet.setFont(font=fuente_seleccionada)

# Imprimir el texto con la fuente seleccionada
print(figlet.renderText(texto_imprimir))