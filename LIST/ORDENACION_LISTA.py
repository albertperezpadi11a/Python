import random

list = []
for i in range(10):
    list.append(random.randrange(100))

print("Unordered list:", list, sep = "\n")

#each step of the "for i" loop guarantees that the list is ordered until list[i]
for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[i] < list[j]:
            aux = list[i]
            list[i] = list[j]
            list[j] = aux

print("Ordered list:", list, sep = "\n")

