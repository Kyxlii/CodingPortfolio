##INFO##
# Make a function that encrypts a given input with these steps:

# Input: "apple"

# Step 1: Reverse the input: "elppa"

# Step 2: Replace all vowels using the following chart:

# a => 0
# e => 1
# i => 2
# o => 3
# u => 4
# EG: "1lpp0"

# Step 3: Add "aca" to the end of the word: "1lpp0aca"

# Output: "1lpp0aca"

##funcs
def encrypt(unencrypted): #Technically incorrect following of steps :P
    encrypted = ""
    for x in unencrypted: #Here x == unencrypted[x].
        if x in vowelKey: #If x matches any primary key in the dictionary \/
            encrypted += vowelKey[x]    #concatinates the encrypted letter into a variable
        else:
            encrypted += x #If x doesn't match, concatinates it as is into the variable
    return encrypted+"aca" #concatinates "aca" to the completed encryption and returns to call.

##main

vowelKey = { #Global dictionary for the encryption key.
    "a" : "0",
    "e" : "1",
    "i" : "2",
    "o" : "2",
    "u" : "3"
}

userWord = input("Which word would you like to encrypt?\n") #User input.

print(f'Your encrypted word is: "{encrypt(userWord[::-1].lower())}"') #[::-1] uses string logic to reverse the word.

#This looks clean as friggle frack without notes btw :D