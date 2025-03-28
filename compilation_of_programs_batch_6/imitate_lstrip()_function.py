#ask user for input
user_input = input("Enter your name with few spaces: ")
#initialize space_count to 0
space_count = 0
#check the characters of the input
for char in user_input:
    #add 1 to space_count if character is space
    if char.isspace():
        space_count += 1
    #break if character is alpha
    else:
        break
#print the input from space_count
print("Output:", user_input[space_count:])