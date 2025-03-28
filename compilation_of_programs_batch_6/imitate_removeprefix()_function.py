#ask for input
user_input = input("Enter a word: ")
#ask what prefix the user wants to remove
prefix_to_remove = input("Enter the prefix you want to remove: ")
#check if the prefix matches the prefix of the user input
if len(prefix_to_remove) <= len(user_input) and user_input[0:len(prefix_to_remove)] == prefix_to_remove:
    #print input with prefix removed if true
    print(user_input[len(prefix_to_remove):])
    #print user input if not 
else:
    print(user_input)