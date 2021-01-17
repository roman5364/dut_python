import math
from random import randint

n = int(input("Enter your number in list: "))
m = int(input("Enter control number: "))
x = [randint(-100, 100) for i in range(10 + n)]

print("Generated list: ", x)
y = []
for i in range(len(x)):
    if math.fabs(x[i]) > m:
        y.append(x[i])
print("List with |X[i]| > M", y)
for i in range(len(x)):
    if x[i] < 0:
        x[i] = int(math.fabs(x[i]))
print("P-numbers list: ", x)
print("Max element: ", max(x))
x.reverse()
print("Reversed list: ", x)

my_len = [['ІT-41',
           ['Акулова Олена Михайлівна', 'Бабушкіна Ксенія Петрівна']],
          ['ІТ-42',
           ['Богдан Андрій Миколайович', 'Пивоваренко Степан Генадійович']],
          ['ІT-43',
           ['Цвік Петро Перший', 'Герман Віктор Валерійович']]]

while 1:
    key = int(input("Select group:\n1. IT-41\n2. IT-42\n3. IT-43\n"))
    if key == 1:
        print("1. ", my_len[0][0], "\n", my_len[0][1])
        break
    elif key == 2:
        print("2. ", my_len[1][0], "\n", my_len[1][1])
        break
    elif key == 3:
        print("3. ", my_len[2][0], "\n", my_len[2][1])
        break
    else:
        print("Incorrect input")
