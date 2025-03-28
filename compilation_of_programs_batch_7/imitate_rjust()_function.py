#ask for input
user_input = input("Enter a word: ")
#ask for space to be added
space_to_add = int(input("Enter how much right adjustment you want: "))
#set adjusted input as space plus the input
adjusted_input = " " * space_to_add + user_input
#print adjusted input
print(adjusted_input)