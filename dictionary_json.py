import json
data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    else:
        print("Word not found!")

word = input("Enter the word you want to search: ")
output = search(word)
print(output)
