import json

def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_dictionary(dictionary, file_path):
    with open(file_path, 'w') as f:
        json.dump(dictionary, f)

def lookup_word(dictionary, word):
    return dictionary.get(word.lower())

def main():
    file_path = "dictionary.json"
    dictionary = load_dictionary(file_path)

    while True:
        user_input = input("\nEnter a word to look up (type 'exit' to quit): ").lower()

        if user_input == 'exit' or user_input == 'quit':
            print("Exiting the app. Goodbye!")
            break

        definition = lookup_word(dictionary, user_input)

        if definition:
            print("\nDefinition(s) for '{}':".format(user_input.capitalize()))
            for idx, item in enumerate(definition, 1):
                print("{}. {}".format(idx, item))
        else:
            print("\nSorry, the word '{}' was not found in the dictionary.".format(user_input.capitalize()))

if __name__ == "__main__":
    main()

