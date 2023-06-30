class TablaMultiplicar:
    def solicitar_numero(self, mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero < 1 or numero > 10:
                    raise ValueError
                return numero
            except ValueError:
                print("Error: Debes introducir un número entero entre 1 y 10.")

    def generar_tabla(self):
        numero = self.solicitar_numero("Introduce un número entre 1 y 10: ")
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")
        print(f"La tabla de multiplicar del número {numero} ha sido generada correctamente.")

    def mostrar_tabla_completa(self):
        numero = self.solicitar_numero("Introduce un número entre 1 y 10: ")
        try:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                contenido = archivo.read()
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo tabla-{numero}.txt no existe.")

    def mostrar_linea_tabla(self):
        numero = self.solicitar_numero("Introduce un número entre 1 y 10: ")
        linea = self.solicitar_numero("Introduce el número de línea a mostrar: ")
        try:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                lineas = archivo.readlines()
                if linea > 0 and linea <= len(lineas):
                    linea_seleccionada = lineas[linea - 1]
                    print(linea_seleccionada)
                else:
                    print("Error: El número de línea especificado no es válido.")
        except FileNotFoundError:
            print(f"El archivo tabla-{numero}.txt no existe.")


def menu():
    tabla_multiplicar = TablaMultiplicar()
    while True:
        print("==== Menú ====")
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla completa")
        print("3. Mostrar línea de la tabla")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            tabla_multiplicar.generar_tabla()
        elif opcion == "2":
            tabla_multiplicar.mostrar_tabla_completa()
        elif opcion == "3":
            tabla_multiplicar.mostrar_linea_tabla()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


menu()
