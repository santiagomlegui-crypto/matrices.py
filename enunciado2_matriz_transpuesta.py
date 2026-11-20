# Enunciado 2: Matriz transpuesta
n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(float(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(fila)

transpuesta = []
for j in range(m):
    fila = []
    for i in range(n):
        fila.append(matriz[i][j])
    transpuesta.append(fila)

ancho = max(len(str(v)) for fila in matriz for v in fila)

print(f"\nMatriz original ({n}x{m}):")
for fila in matriz:
    for v in fila:
        print(str(v).rjust(ancho + 2), end="")
    print()

print(f"\nMatriz transpuesta ({m}x{n}):")
for fila in transpuesta:
    for v in fila:
        print(str(v).rjust(ancho + 2), end="")
    print()
