import random

list = []
for i in range(10):
    list.append(random.randrange(100))

print("Unordered list:", list, sep = "\n")

#each step in the "for element" loop checks an element and the element after it. should the element after it be lower, both elements will swap positions
#the "for element" loop is executed len(list) - 1 times, which is the lowest amount of iterations needed to fully order any list
#J called this the "algoritmo de la burbuja"

for j in range(len(list) - 1):
    for i in range(len(list) - (j + 1)):
        if list[i] > list[i + 1]:
            aux = list[i]
            list[i] = list[i + 1]
            list[i + 1] = aux

print("Ordered list:", list, sep = "\n")