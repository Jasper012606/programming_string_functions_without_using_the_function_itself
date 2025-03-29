#ask for input
user_input = input("Enter a word with trailing spaces: ")
#reverse the string input, remove the spaces and reverse again
input_without_trailing_spaces = user_input[::-1].lstrip()[::-1]
#print input without trailing spaces
print(input_without_trailing_spaces)