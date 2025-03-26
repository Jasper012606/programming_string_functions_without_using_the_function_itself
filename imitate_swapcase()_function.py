#ask for input
user_input = input("Enter first name: ")
#set swapcased input to ""
swapcased_input = ""
#check for each letter of each word
for char in user_input:
    #if lower case
    if char.islower():
        #use upper() then add to swapcased input
        swapcased_input += char.upper()
    #if uppercase
    if char.isupper():
        #use lower() then add to swapcased input
        swapcased_input += char.lower()
#print swapcased input
print(swapcased_input)