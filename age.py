while True:
    try:
        age = int(input("Enter the student's age (16-30):"))
        if age >= 16 and age <= 30:
            print("Age of {0} has been accepted by the system as valid".format(age))
        else:
            print("Age of {0} has not been accepted by the system".format(age))
    except Exception:
        print("An unexpected error has occurred")
