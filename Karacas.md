# Karacas encryption program

This was a small project we were given to encrypt entered text according to a specific rule set:
<ul>
  <li>The word is reversed.</li>
  <li>The vowels are encrypted into numbers (a -> 0, e -> 1, i -> 2, o -> 2, u -> 3)</li>
  <li>"aca" is appended to the end of each word</li>
</ul>
Because of this rule set, decryption is not applicable without applying a dictionary and creating essentially my own spell checker, which while that would be great learning experience, isn't something I think belongs with this task. The program detects if the text is encrypted based on the pattern of "aca" at the end of each word, making the user experience easier.

### [Code:](/Karacas.py)
```python
#Encryption and decryption section

def encrypt(unencrypted):
    '''Seperates the text into words, reverses the word, encrypts the vowels into numbers, appends "aca" to the word, moves onto next word.'''
    return " ".join(["".join([vowelKey[x] if x in vowelKey else x for x in word[::-1]])+"aca" for word in unencrypted])

def decrypt(encrypted):
    '''Seperates the text into words, removes "aca" from the word, decrypts the numbers into vowels, reverses the word, moves onto next word.'''
    return " ".join(["".join([keyVowel[x] if x in keyVowel else x for x in word[:-3]])[::-1] for word in encrypted])


vowelKey = { #Dictionary for the encryption key. Technically incorrect as both i & o are "2" in task description, however this removes errors in decryption.
    "a" : "0",
    "e" : "1",
    "i" : "2",
    "o" : "3",
    "u" : "4"
}
keyVowel = {value : key for key, value in vowelKey.items()} #Dictionary for the decryption key. Uses dictionary comprehension to reverse vowelKey


#Input and output section

userText = input("Text to Karacas:\n").lower().split() #User input. Splits the user's text into an array of strings.

funcType = ["decrypted", decrypt] if all([word[-3:] == "aca" for word in userText]) else ["encrypted", encrypt]

print(f'Your {funcType[0]} {"word" if len(userText) == 1 else "sentence"} is: \"{funcType[1](userText)}\"')
```
### Output:

Encryption
![](/bin/KaracasTO.png)
Decryption
![](/bin/KaracasFROM.png)
