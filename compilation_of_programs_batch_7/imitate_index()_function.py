#ask for input
user_input = input("Enter a word: ")
#ask what user want to find
what_to_find = input("What do you want to find: ")
#use find() and set as result
result = user_input.find(what_to_find)
#if result is -1, print "ValueError: substring not found"
if result == -1:
    print("ValueError: substring not found")
#else print result
else:
    print(result)