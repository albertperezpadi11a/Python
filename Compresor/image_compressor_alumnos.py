import AWS_compression as amsc

# ruta_imagen = input("Ruta o nombre de la imagen a comprimir:\n")
# ruta_imagen_comprimida = input("Ruta o nombre de la imagen comprimida:\n")
ruta_imagen = "logo_esteve.jpeg"
ruta_imagen_comprimida = "aa_logo_comprimido.jpg"

comprimida_r = []
comprimida_g = []
comprimida_b = []
# Leer imagen
matriz_r, matriz_g, matriz_b, ancho, alto = amsc.imagen_a_matrices(ruta_imagen)


######################################################################
##### ESCRIBE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES A CONTINUACIÓN #####
######################################################################
comprimida_r_columnas = []
comprimida_g_columnas = []
comprimida_b_columnas = []

#Red
for row in range(len(matriz_r)):
    comprimida_r_columnas.append([])
    for column in range(0, ancho, 2):
        if len(matriz_r) % 2 == 1 and column == len(matriz_r[0]) - 1:
            comprimida_r_columnas[row].append(matriz_r[row][column])
        else:
            comprimida_r_columnas[row].append(matriz_r[row][column] + matriz_r[row][column + 1] // 2)
for fila in range(0, len(comprimida_r_columnas), 2):
    comprimida_r.append([])
    for columna in range(len(comprimida_r_columnas[0])):
        if len(comprimida_r_columnas) % 2 == 1 and fila == len(comprimida_r_columnas) - 1:
            comprimida_r[fila // 2].append(comprimida_r_columnas[fila][columna])
        else:
            comprimida_r[fila // 2].append(comprimida_r_columnas[fila][columna] + comprimida_r_columnas[fila + 1][columna] // 2)

#Green
for fila in range(0,len(comprimida_b_columnas),2):
    comprimida_b.append([])
    for columna in range(len(comprimida_b_columnas[0])):
        if len(comprimida_b_columnas)%2 == 1 and fila == len(comprimida_b_columnas) -1:
            comprimida_b[fila // 2].append(comprimida_b_columnas[fila][columna])
        else:
            comprimida_b[fila//2].append((comprimida_b_columnas[fila][columna] +comprimida_b_columnas[fila+1][columna])//2  )

#Blue
for row in range(len(matriz_b)):
    comprimida_b_columnas.append([])
    for column in range(0, ancho, 2):
        if len(matriz_b) % 2 == 1 and column == len(matriz_b[0]) - 1:
            comprimida_b_columnas[row].append(matriz_b[row][column])
        else:
            comprimida_b_columnas[row].append(matriz_b[row][column] + matriz_b[row][column + 1] // 2)
for fila in range(0,len(comprimida_g_columnas),2):
    comprimida_g.append([])
    for columna in range(len(comprimida_g_columnas[0])):
        if len(comprimida_g_columnas)%2 == 1 and fila == len(comprimida_g_columnas) -1:
            comprimida_g[fila // 2].append(comprimida_g_columnas[fila][columna])
        else:
            comprimida_g[fila//2].append((comprimida_g_columnas[fila][columna] +comprimida_g_columnas[fila+1][columna])//2  )

# Las matrices de la imagen original son matriz_r, matriz_g y matriz_b
# una para cada canal.
# Crea tres matrices nuevas llamadas: comprimida_r_columnas, comprimida_g_columnas y
# comprimida_b_columnas con el fin de comprimir las matrices de la imagen 
# original.
# Utiliza los diferentes métodos de compresión explicados por el 
# profesor en clase.

######################################################################
##### FINAL DE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES ###################
######################################################################

# Mostrar estadísticas de compresión
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r_columnas, comprimida_g_columnas, comprimida_b_columnas)

# Guardar matriz comprimida
amsc.matrices_a_imagen(comprimida_r_columnas, comprimida_g_columnas, comprimida_b_columnas, ruta_imagen_comprimida)

