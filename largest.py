number = 0
largest = 0

while number >= 0:
    try:
        number = int(input("Enter number: "))
        if number > largest:
            largest = number
    except ValueError:
        print("Type the number correctly!")

print("Largest: {}".format(largest))
