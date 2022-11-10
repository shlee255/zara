def has_backslash(inputString):
    return (' ' in inputString)

def has_space(inputString):
    return (' ' in inputString)

def has_lowercase(inputString):
    return any(char.islower() for char in inputString)

def has_uppercase(inputString):
    return any(char.isupper() for char in inputString)

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

print("Please Input a string with at least one '\\', a space, a lower-case letter, an upper-case letter and a number")
str = input()
while not (has_backslash(str) and has_space(str) and has_lowercase(str) and has_uppercase(str) and has_numbers(str)):
    print("Input Error!  Please Input a string with at least one '\\', a space, a lower-case letter, an upper-case letter and a number")
    str = input()

print(str)
str = str.replace('\\','n')

for ch in str:
    if ch.islower():
        str = str.replace(ch,'\\')
    elif ch.isupper():
        str = str.replace(ch,'t')
    elif ch.isdigit():
        str = str.replace(ch,'*')

print(str)