import math

your_number = int(input("Enter your variant: "))
array = [[1, 3, 4, 5, 6, 7, your_number], [8, 9, 10, 11, your_number, 29, 30], [your_number, 2, 4, 7, 8, 3, 5]]
print(f"List: {array}")

final_array = []
max_element = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = math.sqrt(array[i][j])
        if array[i][j] < 5:
            final_array.append(array[i][j])
        if array[i][j] > max_element:
            max_element = array[i][j]

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = ("%.2f" % array[i][j])

for i in range(len(final_array)):
    final_array[i] = ("%.2f" % final_array[i])

print("First task: ", array)
print("Second task: ", final_array)
print("Third task: ", format(max_element, '.2f'))
