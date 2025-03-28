#ask for user input
user_input = input("Enter any word: ")
#ask the user for the width
width = int(input("Enter the width: "))
#get the total space needed
total_space = width - len(user_input)
#check if total space is greater than 0
if total_space > 0:
    #if true, get the total space for both sides
    left_space = total_space // 2
    right_space = total_space - left_space
        #set centered text plus the spaces
    centered_input = " " * left_space + user_input + " " * right_space
    #else, print text as is
else:
    print(user_input)
#print centered text
print(centered_input)