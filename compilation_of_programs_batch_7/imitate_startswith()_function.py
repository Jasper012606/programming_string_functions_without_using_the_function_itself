#ask for input
user_input = input("Enter a word: ")
#ask what prefix the user wants to check
prefix_to_check = input("You want to check if your word starts with: ")
#check if the prefix matches the prefix of the input
if len(prefix_to_check) <= len(user_input) and user_input[0:len(prefix_to_check)] == prefix_to_check:
    #print True if true
    print(True)
    #print Fale if not true
else:
    print(False)