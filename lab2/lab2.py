import math

# value of function
x = float(input("x = "))
if x < 0:
    y = (math.pow(math.sin(math.pow(x, 2)), 2)) / math.fabs(x + 1)
elif x >= 0:
    y = 0.5 - math.pow(math.fabs(x), 1 / 4)

print(f"value of function:{y}\n")

group_list = [i for i in range(1, 29)]
print('List of items:', group_list)


a = []
for i in range(int(input("Enter list size: "))):
    a.append(int(input()))

print(f"List of items:{a}\n")
print(f"Common list elements:{list(set(a))}")
print(f"Min element in list: {min(a)}\nMax element in list: {max(a)}\n")
