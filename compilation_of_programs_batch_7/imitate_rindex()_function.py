#ask for input
user_input = input("Enter a word: ")
#ask what user wants to find
what_to_find = input("What do you want to find: ")
#use rfind() and set as result
result = user_input.rfind(what_to_find)
#if result is -1, print "Value Error: substring not found"
if result == -1:
    print("ValueError: substring not found")
#else print 
else:
    print(result)