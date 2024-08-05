import pyperclip

with open("numbers.txt") as file:
    numbers = file.readlines()

for number in numbers:
    print(number.strip())
    number = number.strip()
    pyperclip.copy(number)
    print(number, "copied to clipboard")