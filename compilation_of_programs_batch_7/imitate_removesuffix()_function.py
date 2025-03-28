#ask for input
user_input = input("Enter a word: ")
#ask what suffix the user wants to remove
suffix_to_remove = input("Enter the suffix want to remove: ")
#check if suffix matches the suffix of the input
if len(suffix_to_remove) <= len(user_input) and user_input[-len(suffix_to_remove):] == suffix_to_remove:
    #print input without the suffix if true
    print(user_input[0:-len(suffix_to_remove)])
    #print input as is if not true
else:
    print(user_input)