"""
#how to print a matrix (J's format)
matrix = [[3,1,1],[2,1,7],[5,2,8]]
#len(matrix) == 3
data = ""
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print(data)

#how to create a matrix with a given number of rows and columns
import random

matrix = []
data = ""
rows = ""
columns = ""
while not rows.isdigit():
    rows = input("How many rows?\n")
    if not rows.isdigit():
        input("Non-numeric answer. Press enter to continue...")
rows = int(rows)

while not columns.isdigit():
    columns = input("How many columns?\n")
    if not columns.isdigit():
        input("Non-numeric answer. Press enter to continue...")
columns = int(columns)

#for i in range(rows):
for i in range(rows):
    matrix.append([])
    #for j in range(columns):
    for j in range(columns):
        matrix[i].append(random.randint(1, 100))
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print(data)
"""
import random

matrix = []
default_matrix = ""
transposed_matrix = ""
vertical_reflection = ""
horizontal_reflection = ""
whatever_this_is = []
whatever_this_is2 = []
whatever_this_is3 = []
whatever_this_is4 = []
dimension = ""

while not dimension.isdigit():
    dimension = input("Input matrix dimension (nxn):\nn = ")
    if not dimension.isdigit():
        input("Non-numeric answer. Press enter to continue...")
dimension = int(dimension)

for fila in range(dimension):
    matrix.append([])
    for columna in range(dimension):
        matrix[fila].append(random.randint(1, 100))
        default_matrix += str(matrix[fila][columna]).rjust(5)
    default_matrix += "\n"

for fila in range(dimension):
    for columna in range(dimension):
        transposed_matrix += str(matrix[columna][fila]).rjust(5)
    transposed_matrix += "\n"

for fila in range(dimension):
    for columna in range(dimension - 1, -1, -1):
        vertical_reflection += str(matrix[fila][columna]).rjust(5)
    vertical_reflection += "\n"

for fila in range(dimension - 1, -1, -1):
    for columna in range(dimension):
        horizontal_reflection += str(matrix[fila][columna]).rjust(5)
    horizontal_reflection += "\n"

#esto no lo he sacado por mi cuenta, pero casi
#1  2  3            2+3  1+3  1+2
#4  5  6     ==>    5+6  4+6  4+5
#7  8  9            8+9  7+9  7+8
for fila in range(dimension):
    whatever_this_is.append([])
    for columna in range(dimension):
        whatever_this_is[fila].append(0)
        for i in range(dimension):
            if i != columna:
                whatever_this_is[fila][columna] += matrix[fila][i]

wti = ""
for fila in range(len(whatever_this_is)):
    for columna in range(len(whatever_this_is[fila])):
        wti += str(whatever_this_is[fila][columna]).rjust(5)
    wti += "\n"

#1  2  3            4+7  5+8  6+9
#4  5  6     ==>    1+7  2+8  3+9
#7  8  9            1+4  2+5  3+6
for fila in range(dimension):
    whatever_this_is2.append([])
    for columna in range(dimension):
        whatever_this_is2[fila].append(0)
        for i in range(dimension):
            if i != fila:
                whatever_this_is2[fila][columna] += matrix[i][columna]

wti2 = ""
for fila in range(len(whatever_this_is2)):
    for columna in range(len(whatever_this_is2[fila])):
        wti2 += str(whatever_this_is2[fila][columna]).rjust(5)
    wti2 += "\n"

#1  1  1            1  2  1
#1  1  1     ==>    1  2  1
#1  1  1            1  2  1
#each element equals the sum of their original horizontal neighbors
for fila in range(dimension):
    whatever_this_is3.append([])
    for columna in range(dimension):
        whatever_this_is3[fila].append(0)
        for i in range(columna - 1, columna + 2):
            if i != columna and 0 <= i <= dimension - 1:
                whatever_this_is3[fila][columna] += matrix[fila][i]

wti3 = ""
for fila in range(len(whatever_this_is3)):
    for columna in range(len(whatever_this_is3[fila])):
        wti3 += str(whatever_this_is3[fila][columna]).rjust(5)
    wti3 += "\n"

#1  1  1            1  1  1
#1  1  1     ==>    2  2  2
#1  1  1            1  1  1
#each element equals the sum of their original vertical neighbors
for fila in range(dimension):
    whatever_this_is4.append([])
    for columna in range(dimension):
        whatever_this_is4[fila].append(0)
        for i in range(fila - 1, fila + 2):
            if i != fila and 0 <= i <= dimension - 1:
                whatever_this_is4[fila][columna] += matrix[i][columna]

wti4 = ""
for fila in range(len(whatever_this_is4)):
    for columna in range(len(whatever_this_is4[fila])):
        wti4 += str(whatever_this_is4[fila][columna]).rjust(5)
    wti4 += "\n"

print("\nDefault matrix:\n", default_matrix, "\n", sep="")
print("Transposed matrix:\n", transposed_matrix, "\n",sep="")
print("Vertical reflection:\n", vertical_reflection, "\n", sep="")
print("Horizontal reflection:\n", horizontal_reflection, "\n", sep="")
print("Whatever this is:\n", wti, "\n", sep="")
print("Whatever this is 2:\n", wti2, "\n", sep="")
print("Whatever this is 3:\n", wti3, "\n", sep="")
print("Whatever this is 4:\n", wti4, "\n", sep="")