# Enunciado 4: Búsqueda del mayor valor y su posición
n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(float(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(fila)

mayor = matriz[0][0]
pos_fila = 0
pos_col = 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:      # ">" estricto: se queda con la primera aparición
            mayor = matriz[i][j]
            pos_fila = i
            pos_col = j

ancho = max(len(str(v)) for fila in matriz for v in fila)
print("\nMatriz:")
for fila in matriz:
    for v in fila:
        print(str(v).rjust(ancho + 2), end="")
    print()

print("\nValor máximo:", mayor)
print(f"Posición: fila {pos_fila}, columna {pos_col}")
