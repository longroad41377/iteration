number = 0
numbers = []

while number != -1:
    number = int(input("Enter number: "))
    if number != -1:
        numbers.append(number)

total = 0
for n in numbers:
    total += n

average = total / len(numbers)
print("Average: {}".format(average))
