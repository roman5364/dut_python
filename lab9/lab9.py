def generate_cubes(N):
    for i in range(N):
        yield i ** 3


x = 0
y = 0
print(list((x, y) for x in range(7) if x % 2 == 1
           for y in range(7) if y % 2 == 0))

n = int(input("Enter your group list number: "))
A = [[11, n, 44, 55],
     [1, 2, n, 4],
     [11, 12, 13, 14],
     [21, 31, 41, n]]
print("Main diagonal: ", list(A[i][i] for i in range(len(A))))
print("Side diagonal: ", list(A[i][len(A) - 1 - i] for i in range(len(A))))
print("Changed matrix: ", list(list(col + n for col in row) for row in A))
M = [[1, 2, 3, 6],
     [4, 5, 6, 0],
     [7, 8, 9, 7],
     [71, 8, 93, 7]]
print("Multiply of two matrix: ", list(list(A[row][col] * M[row][col] for col in range(4)) for row in range(4)))

for i in generate_cubes(n):
    print(i, end=' : ')
