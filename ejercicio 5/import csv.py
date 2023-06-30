import csv

bitcoin_prices = [
    {"date": "2023-06-01", "price": 35000},
    {"date": "2023-06-02", "price": 35500},
    {"date": "2023-06-03", "price": 36000},
    {"date": "2023-06-30", "price": 38000}
]

# Guardar en un archivo de texto (txt)
with open("bitcoin_prices.txt", "w") as txt_file:
    for price in bitcoin_prices:
        txt_file.write(f"{price['date']}: {price['price']}\n")

# Guardar en un archivo CSV
fieldnames = ["date", "price"]

with open("bitcoin_prices.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(bitcoin_prices)
