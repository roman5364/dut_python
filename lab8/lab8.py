import math


def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fibonacci(n - 1)
        lst.append(lst[-1] + lst[-2])
        return lst


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


n = int(input("Enter your variant: "))
print("Result for ", n, " + 10 = ", fibonacci(n + 10))
print("Result for ", n, " + 10! = ", factorial(n + 10))
print("Lambda func out: ")
L = [lambda x: x + n,
     lambda x: math.pow(x, 6),
     lambda x: x - 2,
     lambda x: math.pow(x, 2)]
for i in L:
    print(i(n + 3))