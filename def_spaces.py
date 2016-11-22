def count_spaces(string):
    spaces = 0
    for char in string:
        if char == " ":
            spaces += 1
    return spaces

def main():
    user_input = input("Please enter a sentence: ")
    print("In your sentence", count_spaces(user_input), "spaces.")

main()
