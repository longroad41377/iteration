#Binary converter
#Challenge exercises 2

number = int(input("Enter number: "))

digits = ""
digit = 7

while digit >= 0:
    if number >= 2 ** digit:
        digits += "1"
    else:
        digits += "0"

    number = number % (2 ** digit)
    digit -= 1

print(digits)
