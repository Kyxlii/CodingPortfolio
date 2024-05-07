# Pig Latin encryptor

This program takes a sentence from the user, breaks it down into each word, converts each word into [Pig Latin](https://web.ics.purdue.edu/~morelanj/RAO/prepare2.html) and prints them.

## [Code](PigLatin.py):
```python
#func
def consonantHandler(pigWord):
    '''if special cases aren't met, this function finds the first case of a vowel and sorts the word based on its location.'''
    wordLength = len(pigWord)
    for i in range(wordLength): #enumerate would also work here. 
        if pigWord[i] in vowels:
            return pigWord[i:] + pigWord[:i] + "ay"
    return pigWord[2:] + pigWord[:2] + "ay" #information is inconsistent about what to do when all letters are consonants. 

def pigCalc(pigWord):
    '''sorting word into the relevant category for an accurate translation.'''
    if len(pigWord) == 1:
        return pigWord + "ay"
    if pigWord[0] in vowels:
        return pigWord + "way"
    if pigWord[0:2] == "qu":
        return pigWord[2:] + pigWord[:2] + "ay"
    else:
        return consonantHandler(pigWord)

##main
vowels = ["a", "e", "i", "o", "u"] #global variable to reduce redundancy
userText = str(input("What sentence would you like to convert to Pig Latin?\n")).split() #input is split into array here also to reduce redundancy

textType = "sentence" if len(userText) > 1 else "word"
pigString = " ".join([pigCalc(word.lower()) for word in userText])

print(f"Your {textType} in Pig Latin is:\n{pigString}")
```

### Output:

![An image containing the output of the code.](bin/igLatinOutputPay.png)

## [Return to portfolio here.](README.md)
