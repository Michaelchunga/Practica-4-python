import requests

# Solicitar al usuario la cantidad de bitcoins
n = float(input("Ingrese la cantidad de bitcoins que posee: "))

try:
    # Consultar la API de CoinDesk
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()

    # Obtener el precio actual de Bitcoin en USD
    price_usd = data["bpi"]["USD"]["rate_float"]

    # Calcular el costo actual de "n" Bitcoins en USD
    cost_usd = n * price_usd

    # Mostrar el costo actual con cuatro decimales y separador de miles
    print(f"El costo actual de {n:,.8f} Bitcoins es de ${cost_usd:,.4f} USD")

except requests.RequestException:
    print("Ocurrió un error al consultar la API de CoinDesk.")
