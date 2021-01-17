from random import randint

k = int(input("Enter your variant: "))
r = 3
array = [[1, 7, k], [8, k, 29], [k, 2, 4]]
print(f"List: {array}\n")


def get_min_in_column(column_number):
    min_in_column = array[column_number][0]
    for item in array[column_number]:
        if min_in_column > item:
            min_in_column = item
    return min_in_column


print("Max in second array column: ", get_min_in_column(1))
print("Min in third array column: ", get_min_in_column(2))

print("Third task: ")
array = []
m = int(input("Enter row number: "))
n = int(input("Enter column number: "))


def fill_2d_array(m, n):
    for i in range(m):
        b = []
        for j in range(n):
            b.append(randint(-10, 10))
        array.append(b)
    return array


fill_2d_array(m, n)

print(f"In List: {array}")


def process_array():
    for i in range(m):
        for j in range(n):
            if array[i][j] < 0:
                array[i][j] = 0
            elif array[i][j] > 0:
                array[i][j] = 1


process_array()

print(f"Processed list: {array}")
