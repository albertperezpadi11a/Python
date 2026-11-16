import random

# lista = []
# for i in range(5):
#     lista.append(random.randrange(0, 100))
# print(lista)
#
# for step in range(len(lista) - 1):
#     print("Steps = {}".format(step).center(30, "*"))
#     for i in range(len(lista) - 1, step, -1):
#         print("Compare {} with {}".format(i, i - 1))
#         if lista[i] > lista[i - 1]:
#             aux = lista[i]
#             lista[i] = lista[i - 1]
#             lista[i - 1] = aux
# print(lista)

matrix = []
dimension = 3
data = ""
for i in range(dimension):
    matrix.append([])
    for j in range(dimension):
        matrix[i].append(random.randrange(100))
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print("Unordered matrix:", data, sep="\n")

for row in range(dimension):
    for step in range(dimension - 1):
        for i in range(dimension - 1, step, - 1):
            if matrix[row][i] < matrix[row][i - 1]:
                aux = matrix[row][i]
                matrix[row][i] = matrix[row][i - 1]
                matrix[row][i - 1] = aux

for column in range(dimension):
    for step in range(dimension - 1):
        for i in range(dimension - 1, step, - 1):
            if matrix[i][column] < matrix[i - 1][column]:
                aux = matrix[i][column]
                matrix[i][column] = matrix[i - 1][column]
                matrix[i-1][column] = aux

data = ""
for i in range(dimension):
    for j in range(dimension):
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print("Ordedered matrix:", data, sep="\n")
