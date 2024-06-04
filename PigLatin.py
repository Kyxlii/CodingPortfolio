#func
def consonantHandler(pigWord):
    '''if special cases aren't met, this function finds the first case of a vowel and sorts the word based on its location.'''
    for i, pigChar in enumerate(pigWord): #implimented enumerate. this should be faster and more consise.
        if pigChar in vowels:
            return pigWord[i:] + pigWord[:i] + "ay"
    return pigWord[2:] + pigWord[:2] + "ay" #information is inconsistent about what to do when all letters are consonants. 


def punctuationHandler(pigWord):
    '''attempts to handle punctuation in entered text by seperating characters unrecognised in the "letters" list from recognised characters.'''
    pigWordWithoutPunc, puncInPigWord = "", ""
    
    for char in pigWord:
        if char in letters:
            pigWordWithoutPunc += char
        else:
            puncInPigWord += char

    return pigWordWithoutPunc, puncInPigWord


def pigSorting(pigWord):
    '''sorting word into the relevant category for an accurate translation.'''
    if not all([char in letters for char in pigWord]):
        pigWord, punctuation = punctuationHandler(pigWord)
    else:
        punctuation = ""
    if len(pigWord) == 1:
        return pigWord + "ay" + punctuation
    if pigWord == "":
        return punctuation
    if pigWord[0] in vowels:
        return pigWord + "way" + punctuation
    if pigWord[0:2] == "qu":
        return pigWord[2:] + pigWord[:2] + "ay" + punctuation
    else:
        return consonantHandler(pigWord) + punctuation


##main
vowels = {"a", "e", "i", "o", "u"} # as these are only used for membership checks, they're stored as sets.
letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "("}
userText = input("What sentence would you like to convert to Pig Latin?\n").lower().split() #input is split into array here also to reduce redundancy

textType = "sentence" if len(userText) > 1 else "word"
pigString = " ".join([pigSorting(word) for word in userText])

print(f"\nYour {textType} in Pig Latin is:\n{pigString}")
