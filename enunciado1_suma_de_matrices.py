# Enunciado 1: Suma de dos matrices
print("--- Matriz A ---")
filas_a = int(input("Número de filas: "))
cols_a = int(input("Número de columnas: "))
print("--- Matriz B ---")
filas_b = int(input("Número de filas: "))
cols_b = int(input("Número de columnas: "))

if filas_a != filas_b or cols_a != cols_b:
    print("Error: las matrices deben tener las mismas dimensiones.")
else:
    A = []
    print("\nIngrese los valores de A:")
    for i in range(filas_a):
        fila = []
        for j in range(cols_a):
            fila.append(float(input(f"A[{i}][{j}]: ")))
        A.append(fila)

    B = []
    print("\nIngrese los valores de B:")
    for i in range(filas_b):
        fila = []
        for j in range(cols_b):
            fila.append(float(input(f"B[{i}][{j}]: ")))
        B.append(fila)

    resultado = []
    for i in range(filas_a):
        fila = []
        for j in range(cols_a):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    ancho = max(len(str(v)) for fila in resultado for v in fila)
    print("\nMatriz resultante (A + B):")
    for fila in resultado:
        for v in fila:
            print(str(v).rjust(ancho + 2), end="")
        print()
