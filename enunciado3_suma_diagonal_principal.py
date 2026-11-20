# Enunciado 3: Suma de la diagonal principal
filas = int(input("Número de filas: "))
cols = int(input("Número de columnas: "))

if filas != cols:
    print("Error: la matriz debe ser cuadrada.")
else:
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            fila.append(float(input(f"Elemento [{i}][{j}]: ")))
        matriz.append(fila)

    suma = 0
    for i in range(filas):
        suma += matriz[i][i]

    ancho = max(len(str(v)) for fila in matriz for v in fila)
    print("\nMatriz:")
    for fila in matriz:
        for v in fila:
            print(str(v).rjust(ancho + 2), end="")
        print()

    print("\nSuma de la diagonal principal:", suma)
