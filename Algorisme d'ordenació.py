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

"""
list = []
for j in range(10):
    list.append(random.randrange(100))
print(list)
for pivote in range(len(list) - 1):
    for i in range(pivote + 1, len(list)):
        if list[pivote] < list[i]:
            aux = list[pivote]
            list[pivote] = list[i]
            list[i] = aux
print(list)
"""