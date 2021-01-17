
# сума цифр числа
def sum_of_number(number):
    summa = 0
    while number > 0:
        digit = number % 10
        summa = summa + digit
        number = number // 10
    print("Sum:", summa)


n = int(input("Enter the number: "))
sum_of_number(n)


