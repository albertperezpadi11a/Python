# Exercici 1
var = "La casa blau"
print(var[:])

# Exerici 2
list = [1, [2, [3, 4]], 5]
print(list)
list.insert(2, [6, 7])
print(list)

# Exercici 3
for i in range(65, 91):
    print(chr(i), end=" ")
print()

# Exercici 4
list = []
for i in range(97, 123):
    for j in range(0, 10):
        list.append((j, chr(i)))
print(list)

# Exericici 5
first = []
last = []
for i in range(97, 123):
    if chr(i) <= "k":
        first.append(chr(i))
    else:
        last.append(chr(i))
print("First letters:", first)
print("Last letters:", last)
