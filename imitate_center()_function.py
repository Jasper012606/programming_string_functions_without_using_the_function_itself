#ask for user input
user_input = input("Enter any word: ")
#ask the user for the width
width = int(input("Enter the width: "))
#get the total space needed
total_space = width - len(user_input)
#check if total space is greater than 0
    #if true, get the total space for both sides
        #set centered text plus the spaces
    #else, print text as is
#print centered text