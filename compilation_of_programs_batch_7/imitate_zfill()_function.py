#ask for input
user_input = input("Enter a word: ")
#ask for width
width = int(input("Enter width: "))
#get the number of spaces left
spaces = width - len(user_input )
#if spaces are greater than 0
if spaces > 0:
    #print "0" times the number of spaces plus input
    print("0" * spaces + user_input)
#else
else:
    #print the input
    print(user_input)