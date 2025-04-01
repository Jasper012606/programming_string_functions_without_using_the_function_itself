#make a function
def imitate_count(input, what_to_count):
    #initialize count to 0
    count = 0
    #check for character from the input
    for char in input:
        #if char matches what the user wants to count
        if char == what_to_count:
            #add 1 to count
            count += 1
    #return count
    return count
#ask for input
user_input = input("Enter a short phrase: ")
#ask what the user wants to count from the input
what_to_count = input("What do you want to count: ")
#call and print the function
print(imitate_count(user_input, what_to_count))