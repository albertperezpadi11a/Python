import random

matrix = []
dimension = 3
data = ""
for i in range(dimension):
    matrix.append([])
    for j in range(4):
        matrix[i].append(random.randrange(100))
        data += str(matrix[i][j]).rjust(5)
    data += "\n"

print("Unordered matrix:", data, sep = "\n")

for row in range(len(matrix)):
    for j in range(len(matrix[row]) - 1):
        for i in range(len(matrix[row]) - (j + 1)):
            if matrix[row][i] > matrix[row][i + 1]:
                aux = matrix[row][i]
                matrix[row][i] = matrix[row][i + 1]
                matrix[row][i + 1] = aux

data = ""
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print("Horizontally ordered matrix:", data, sep = "\n")

for column in range(len(matrix[0])):
    for j in range(len(matrix) - 1):
        for i in range(len(matrix) - (j + 1)):
            if matrix[i][column] > matrix[i + 1][column]:
                aux = matrix[i][column]
                matrix[i][column] = matrix[i + 1][column]
                matrix[i + 1][column] = aux

data = ""
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print("Vertically ordered matrix:", data, sep = "\n")