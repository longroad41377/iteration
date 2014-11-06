total = 0
number_count = int(input("Please enter the number of numbers in the series: "))

for counter in range(number_count):
    total += int(input("Please enter number {0} in the series: ".format(counter)))

print("The total of the numbers you entered is {0}".format(total))
