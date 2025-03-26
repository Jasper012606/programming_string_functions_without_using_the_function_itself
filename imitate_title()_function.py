#ask for input then use split() function
user_input = input("Enter your name: ").split()
#set the input in titled casing variable to ""
titled_casing = ""
#make the first letter for each word uppercase and remaining letters lower case then add to titled_casing
for word in user_input:
    titled_casing += (word[0].upper() + word[1:].lower()) + " " #Add " " to seperate each word
#print tinput in titled casing