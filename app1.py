import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):

        w = w.lower()

        if w in data:
            return data[w]

        # Nouns - Ex: Delhi, New York
        elif w.title() in data:
            return data[w.title()]

        # Ex: USA, NATO
        elif w.upper() in data:
            return data[w.upper()]

        # get_close_matches returns a list
        # Make sure list is not empty
        # Get the first value in the list because
        # it has the highest matching ratio
        elif len(get_close_matches(w, data.keys())) > 0:
            match = get_close_matches(w, data.keys())[0]
            yn = input("Did you mean %s instead? (Y/N)" % match)

            while True:
                if yn.lower() == 'y':
                    print()
                    return data[match]
                    break
                elif yn.lower() == 'n':
                    print()
                    return "Word does not exist."
                    break
                else:
                    yn = input("Invalid input. Enter (Y/N). ")

        else:
            return "Word does not exist."

def run():

    choice = ''

    while choice != 2:

        print("[1] Press 1 to enter a word ")
        print("[2] Press 2 to quit ")

        choice = input()

        if choice == '1':

            word = input("Enter a word: ")
            output = translate(word)

            # prints all the definitions in the list if there is more than 1
            # else, prints a string output because otherwise it won't print out properly
            if type(output) == list:
                for definition in output:
                    print(definition)
            else:
                print(output)

        elif choice == '2':
            print("Terminated...")
            break;

        else:
            print("Invalid input.\n")

        print()

run()
