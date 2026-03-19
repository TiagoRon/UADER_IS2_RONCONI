#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* calcula la cantidad de iteraciones de la conjetura de Collatz           *
#* para números entre 1 y 10000 y genera un gráfico                        *
#*-------------------------------------------------------------------------*

import matplotlib.pyplot as plt

# Función que calcula la cantidad de iteraciones hasta llegar a 1
def collatz_iteraciones(n):
    contador = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        contador += 1

    return contador


def main():
    numeros = []
    iteraciones = []

    # Calcular para números del 1 al 10000
    for i in range(1, 10001):
        numeros.append(i)
        iteraciones.append(collatz_iteraciones(i))

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(iteraciones, numeros, s=1)

    plt.title("Conjetura de Collatz (1 a 10000)")
    plt.xlabel("Cantidad de iteraciones")
    plt.ylabel("Número inicial (n)")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()