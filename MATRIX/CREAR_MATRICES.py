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

for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(random.randint(1, 100))
        data += str(matrix[i][j]).rjust(5)
    data += "\n"
print(data)
