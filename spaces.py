user_input = input("Enter a sentence: ")
spaces = 0
for char in user_input:
    if char == " ":
        spaces = spaces + 1
        print(spaces)
        

