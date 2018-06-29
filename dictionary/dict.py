import json

from difflib import get_close_matches

data = json.load(open('data.json'))


def search(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        suggest = get_close_matches(word, data, n=1, cutoff=0.8)
        if suggest:
            y_or_n = input("Did you mean '{}'? Enter 'Y' or 'N': ".format(suggest[0])).lower()
            if y_or_n == 'y':
                return data[suggest[0]]
            elif y_or_n == 'n':
                return "It seems we can't find the word!"
            else:
                return "We can't recognize your answer :("
        else:
            return "It seems we can't find the word!"


user_input = input('Input word: ').lower()

output = search(user_input)

if type(output) == str:
    print(output)
else:
    for item in output:
        print(item)



