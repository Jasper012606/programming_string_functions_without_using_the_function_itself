#ask for input
user_input = input("Enter a word: ")
#ask what suffix the user wants to check
suffix_to_check = input("You want to check if your word ends with: ")
#check if the suffix matches the suffix of the user input
if len(suffix_to_check) <= len(user_input) and user_input[-len(suffix_to_check):] == suffix_to_check:
    #print True if true
    print("True")
    #print False if not true
else:
    print("False")