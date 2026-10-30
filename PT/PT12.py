# Exercici 1
var = "La casa blau"
print(var[:])

# Exerici 2
list1 = [1, [2, [3, 4]], 5]
print(list1)
list1.insert(2, [6, 7])
print(list1)

# Exercici 3
for i in range(65, 91):
    print(chr(i), end=" ")
print()

# Exercici 4
list2 = []
for i in range(97, 123):
    for j in range(0, 10):
        list2.append((j, chr(i)))
print(list2)

# Exericici 5
#a
first = []
last = []
for i in range(97, 123):
    if chr(i) <= "k":
        first.append(chr(i))
    else:
        last.append(chr(i))
print("First letters:", first)
print("Last letters:", last)

#b
quadrant1 = []
quadrant2 = []
quadrant3 = []
quadrant4 = []
for i in range(360):
    quadrant = int( i % 360 / 90)
    if quadrant == 0:
        quadrant1.append(i)
    elif quadrant == 1:
        quadrant2.append(i)
    elif quadrant == 2:
        quadrant3.append(i)
    else:
        quadrant4.append(i)
print("Quadrant1:\n", quadrant1)
print("Quadrant2:\n", quadrant2)
print("Quadrant3:\n", quadrant3)
print("Quadrant4:\n", quadrant4)

#Exercici 6
