import requests
import sqlite3
from datetime import datetime

# Obtener los datos de la API de CoinDesk
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price_usd = data["bpi"]["USD"]["rate_float"]
    price_gbp = data["bpi"]["GBP"]["rate_float"]
    price_eur = data["bpi"]["EUR"]["rate_float"]

    # Conectar a la base de datos
    conn = sqlite3.connect("cryptos.db")
    c = conn.cursor()

    # Crear la tabla si no existe
    c.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                 (date TEXT, usd REAL, gbp REAL, eur REAL)''')

    # Obtener la fecha actual
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insertar los datos en la tabla
    c.execute("INSERT INTO bitcoin VALUES (?, ?, ?, ?)", (date, price_usd, price_gbp, price_eur))
    conn.commit()

    # Cerrar la conexión a la base de datos
    conn.close()

    # Imprimir el precio formateado
    print(f"USD: ${price_usd:,.4f}")
    print(f"GBP: £{price_gbp:,.4f}")
    print(f"EUR: €{price_eur:,.4f}")

except requests.RequestException as e:
    print(f"Error al realizar la solicitud: {str(e)}")
except KeyError:
    print("Error al analizar los datos de la API")
