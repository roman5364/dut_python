import math


# Чи є три трикутника рівновеликими
def is_triangles_are_equal(x, y, z):
    p = (x + y + z) / 2
    result = math.sqrt(p * (p - x) * (p - y) * (p - z))
    return result


print("Чи є три трикутника рівновеликими")
array = []
for i in range(3):
    print("Enter edge of ", i + 1, " triangle")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    array.append(is_triangles_are_equal(a, b, c))
for i in range(3):
    print("Square of ", i + 1, " triangle {:.2f}".format(array[i]))
if array[0] == array[1]:
    if array[1] == array[2]:
        print("Triangles is equal")
else:
    print("Triangles isn't equal")
