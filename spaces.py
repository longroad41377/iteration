while 1:
    string =  input("Enter phrase: ")
    spaces = 0

    for char in string:
        #print(char)
        if char == " ":
            #print("<space>")
            spaces += 1
            

    print("Number of words is {}".format(spaces + 1))
