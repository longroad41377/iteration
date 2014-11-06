while True:
    number = int(input("Enter number: "))
    answer = True

    for count in range(2, number-1):
        remainder = number % count
        if remainder == 0:
            anwser = False

    print(answer)
