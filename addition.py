# program to prompt for 8 numbers and report the total to the user
total = 0
for i in range(1, 9):
	total += int(input('Enter number {} : '.format(i)))

print('The total is {0}'.format(total))
