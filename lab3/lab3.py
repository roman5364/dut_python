# Palindrome check
string = input("Enter a line: ")

# remove all whitespace in a string
my_str = string.replace(" ", "")
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# other
s2 = input("Enter new line: ")
string = str()
print(f"Upper: {s2.upper()}")
print(f"Lower: {s2.lower()}")
print(f"first Upper, other Lower: : {s2.title()}")

t = 0
for i in range(len(s2)):
    if s2[i] != "а":
        string += s2[i]
    else:
        string += "о"
        t += 1
print(f"All a is o: {string}\nTotal changes count: {t}")
