#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de uno o varios números                            *
#* Soporta:                                                                *
#*   - Número único (ej: 5)                                                 *
#*   - Rango (ej: 4-8)                                                      *
#*   - Sin límite inferior (ej: -10 → 1 a 10)                               *
#*   - Sin límite superior (ej: 8- → 8 a 60)                                *
#*-------------------------------------------------------------------------*

import sys

# Función que calcula el factorial de un número
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Función que interpreta la entrada del usuario
def procesar_entrada(entrada):

    # Caso: rango con "-"
    if "-" in entrada:

        partes = entrada.split("-")

        # Caso: "-hasta" → desde 1 hasta N
        if partes[0] == "":
            try:
                fin = int(partes[1])  # convertir a entero
                inicio = 1
            except:
                print("Entrada inválida")
                return

        # Caso: "desde-" → desde N hasta 60
        elif partes[1] == "":
            try:
                inicio = int(partes[0])  # convertir a entero
                fin = 60
            except:
                print("Entrada inválida")
                return

        # Caso: "desde-hasta"
        else:
            try:
                inicio = int(partes[0])  # convertir a entero
                fin = int(partes[1])     # convertir a entero
            except:
                print("Entrada inválida")
                return

        # Validación de rango
        if inicio > fin:
            print("El valor inicial debe ser menor o igual al final")
            return

        # Cálculo de factoriales en el rango
        for i in range(inicio, fin + 1):
            print(f"Factorial {i}! es {factorial(i)}")

    else:
        # Caso: número único
        try:
            num = int(entrada)  # convertir a entero
            print(f"Factorial {num}! es {factorial(num)}")
        except:
            print("Entrada inválida")


# ------------------ Programa principal ------------------

# Si se pasa argumento por línea de comandos
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    # Si no, pedir ingreso manual
    entrada = input("Ingrese un número o rango (ej: 4-8, -10, 8-): ")

# Procesar la entrada
procesar_entrada(entrada)