isogram=input("Please enter a word: ")
word=isogram.lower()
for letter in word:
    if word.count(letter)>1:
        print("Not an isogram")
        break
    else:
        print(f"{isogram} is an Isogram")
        break