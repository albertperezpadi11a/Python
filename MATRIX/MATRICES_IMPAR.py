import random

dimension = 5
matriz = []
for fila in range(dimension):
    matriz.append([])
    for coluna in range(dimension):
        matriz[fila].append(random.randrange(0, 20, 2))
# imprimimos
datos = ""
for fila in range(dimension):
    for columna in range(dimension):
        datos = datos + str(matriz[fila][columna]).rjust(dimension)
    datos = datos + "\n"
print(datos)

matriz_comprimida_columnas = []
for fila in range(dimension):
    matriz_comprimida_columnas.append([])
    for columna in range(0, dimension, 2):
        if len(matriz) % 2 == 1 and columna == len(matriz[0]) - 1:
            matriz_comprimida_columnas[fila].append(matriz[fila][columna])
        else:
            matriz_comprimida_columnas[fila].append(matriz[fila][columna] + matriz[fila][columna + 1] // 2)
# imprimimosç
print("Matriz comprimida por columnas")
datos = ""
for fila in range(len(matriz_comprimida_columnas)):
    for columna in range(len(matriz_comprimida_columnas[0])):
        datos = datos + str(matriz_comprimida_columnas[fila][columna]).rjust(dimension)
    datos = datos + "\n"
print(datos)

print("-----------------------")

matriz_comprimida_columnas_filas = []
for fila in range(0, len(matriz_comprimida_columnas), 2):
    matriz_comprimida_columnas_filas.append([])
    for columna in range(len(matriz_comprimida_columnas[0])):
        if len(matriz_comprimida_columnas) % 2 == 1 and fila == len(matriz_comprimida_columnas) - 1:
            matriz_comprimida_columnas_filas[fila // 2].append(matriz_comprimida_columnas[fila][columna])
        else:
            matriz_comprimida_columnas_filas[fila // 2].append(matriz_comprimida_columnas[fila][columna] + matriz_comprimida_columnas[fila + 1][columna] // 2)
# imprimimosç
print("Matriz comprimida por columnas y filas")
datos = ""
for fila in range(len(matriz_comprimida_columnas_filas)):
    for columna in range(len(matriz_comprimida_columnas_filas[0])):
        datos = datos + str(matriz_comprimida_columnas_filas[fila][columna]).rjust(dimension)
    datos = datos + "\n"
print(datos)