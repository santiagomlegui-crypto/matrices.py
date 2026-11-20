# Enunciado 5: Multiplicación de una matriz por un escalar
n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        while True:
            try:
                valor = float(input(f"Elemento [{i}][{j}]: "))
                break
            except ValueError:
                print("Valor no numérico, intente de nuevo.")
        fila.append(valor)
    matriz.append(fila)

while True:
    try:
        escalar = float(input("Escalar: "))
        break
    except ValueError:
        print("Valor no numérico, intente de nuevo.")

resultado = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(matriz[i][j] * escalar)
    resultado.append(fila)

ancho = max(len(str(v)) for fila in matriz + resultado for v in fila)

print("\nMatriz original:")
for fila in matriz:
    for v in fila:
        print(str(v).rjust(ancho + 2), end="")
    print()

print(f"\nMatriz x {escalar}:")
for fila in resultado:
    for v in fila:
        print(str(v).rjust(ancho + 2), end="")
    print()
