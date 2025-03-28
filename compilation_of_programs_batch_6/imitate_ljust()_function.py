#ask for input
user_input = input("Enter any word: ")
#ask for space to be added
space_to_add = int(input("Enter how much left adjustment you want: "))
#set adjusted input as space plus the input
adjusted_input = user_input + " " * space_to_add 
#print the adjusted input
print(adjusted_input)
