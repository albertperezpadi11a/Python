# Exercici 1
a = (2, 10, 1991)
b = (25, 12, 1990)
c = ("Donald", True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

print(a < b)
# True
print(y + w)
# 12
print(x + a)
# (27, 3, 2, 10, 1991)
print(len(v))
# 2
print(v[1][1])
# 10
print(c[0][0])
# D
print(z, y)
# 27, 9
print(a + b[1:5])
# ?
print((a + b)[1:5])
# ?
print(str(a[2]) + str(b[2]))
# 19911990
print(str(a[2] + b[2]))
# 3981
print(str((a + b)[2]))
# ?
print(str(a + b)[2])
# ?

# Exercici 2
days_month = [31, 28, 31, 30,
31, 30, 31, 31,
30, 31, 30, 31]
day = int(input("Introduce a day: "))
month = int(input("Introduce a month: "))
year = int(input("Introduce a year: "))
date = (year, month, day)
if month == 12 and day == days_month[month - 1]:
    year += 1
    month = 1
    day = 1
elif day == days_month[month - 1]:
    day = 1
    month += 1
else:
    day += 1
following_date = (year, month, day)
print("The following day of {} is {}".format(date, following_date))