import random

largest_number = 0
for count in range(20):
    random_number = random.randint(1,100)
    largest_number = max(largest_number, random_number)

print("The largest random number generated is {0}".format(largest_number))
