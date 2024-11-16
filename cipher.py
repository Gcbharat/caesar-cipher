# add your code here
plain_text = input("Please Enter a sentence:- ")

#Converting the input text into its lower case
plain_text = plain_text.lower()

#Iniatizing the encrypted text
cipher_text = ""
shift_value = 5

for char in plain_text:
    if('a'<=char<='z'):
        new_character = chr((ord(char)-ord('a')+shift_value)%26+ord('a'))
        cipher_text+=new_character
    else:
        cipher_text+=char

#Output
print("The orginal sentence is",plain_text)
print("The Encrpyted sentence is",cipher_text)