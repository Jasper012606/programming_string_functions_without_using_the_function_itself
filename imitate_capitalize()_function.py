#ask user for input
user_input = input("Enter a statement: ")
#set the capitalized_input to ""
capitalized_input = ""
#make the first letter of the input in uppercase and the rest in lowercase
for char in user_input:
    #set the modified input to capitalized_input
    capitalized_input = (user_input[0].upper() + user_input[1:].lower())
#print the capitalized input
print(capitalized_input)