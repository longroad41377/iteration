string = input("Enter string: ")

backwards = ""
for i in range(1, len(string)+1):
    backwards += string[-i]

print(backwards)
