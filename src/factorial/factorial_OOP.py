#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* versión orientada a objetos del cálculo de factorial                    *
#* Soporta: número único, rangos, -N y N-                                  *
#*-------------------------------------------------------------------------*

import sys

class Factorial:
    # Constructor de la clase
    def __init__(self):
        pass

    # Método para calcular factorial de un número
    def calcular(self, num):
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

    # Método principal que ejecuta el cálculo en un rango
    def run(self, minimo, maximo):
        if minimo > maximo:
            print("El valor mínimo debe ser menor o igual al máximo")
            return

        for i in range(minimo, maximo + 1):
            resultado = self.calcular(i)
            print(f"Factorial {i}! es {resultado}")


# Función para interpretar la entrada
def procesar_entrada(entrada):
    fact = Factorial()

    if "-" in entrada:
        partes = entrada.split("-")

        # Caso: -N → 1 a N
        if partes[0] == "":
            try:
                minimo = 1
                maximo = int(partes[1])
            except:
                print("Entrada inválida")
                return

        # Caso: N- → N a 60
        elif partes[1] == "":
            try:
                minimo = int(partes[0])
                maximo = 60
            except:
                print("Entrada inválida")
                return

        # Caso: N-M
        else:
            try:
                minimo = int(partes[0])
                maximo = int(partes[1])
            except:
                print("Entrada inválida")
                return

    else:
        # Número único
        try:
            minimo = maximo = int(entrada)
        except:
            print("Entrada inválida")
            return

    # Ejecutar cálculo
    fact.run(minimo, maximo)


# ------------------ Programa principal ------------------

if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un número o rango (ej: 4-8, -10, 8-): ")

procesar_entrada(entrada)