from random import randint


def fill_an_array(start, end):
    arr = []
    for item in range(randint(start, end)):
        arr.append(int(randint(1, 20)))
    return arr


def get_average(arr):
    summa = 0
    for item in range(len(arr)):
        summa += arr[item]
    print("Sum: ", summa)
    print("Average: ", summa / len(arr))


print("Get Average")
# init arrays
arr1, arr2, arr3 = [], [], []

arr1 = fill_an_array(1, 15)
print(f"the first array: {arr1}")
get_average(arr1)

arr2 = fill_an_array(1, 15)
print(f"the second array: {arr2}")
get_average(arr2)

arr3 = fill_an_array(1, 15)
print(f"the third array: {arr3}")
get_average(arr3)
