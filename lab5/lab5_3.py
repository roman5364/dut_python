def process_arrays(c):
    tmp = c[0]
    c[0] = c[len(c) - 1]
    c[len(c) - 1] = tmp


array = []
m = int(input("Enter array length: "))
for i in range(m):
    print("Enter ", i + 1, " element")
    array.append(int(input()))

print(f"original array: {array}")
process_arrays(array)
print(f"processed array: {array}")
