import random


class Person:
    def __init__(self, name, surname, mark):
        self.name = name
        self.surname = surname
        self.mark = mark

    def __del__(self):
        if self.mark == 1:
            print(self.name, self.surname, ", Ви отримали стипендію.")
        else:
            print(self.name, self.surname, ", Ви залишились бідним.")

    def out(self):
        return self.name, self.surname, self.mark


mark = [0, 1, 0, 1]
random.shuffle(mark)

a = Person("John", "Dou", mark[0])
b = Person("Joe", "Johnson", mark[1])
c = Person("Mike", "Lee", mark[2])
print(a.out())
print(b.out())
print(c.out())
del a
del b
del c
input()
