# Import the dictionary from the external module
from dictionaryD import dictionary

# Valid parts of speech
valid_parts_of_speech = ["noun", "pronoun", "verb", "adjective", "adverb", "preposition", "conjunction", "interjection"]

# Function to add a new word
def add_word(dictionary):
    word = input("Enter the word: ")
    meaning = input(f"Enter the meaning of '{word}': ")

    # Validate the part of speech
    while True:
        part_of_speech = input(f"Enter the part of speech for '{word}': ").lower()
        if part_of_speech in valid_parts_of_speech:
            break
        else:
            print("Error: Invalid part of speech. Please enter one of the following:")
            print(", ".join(valid_parts_of_speech))

    # Additional prompts based on part of speech
    if part_of_speech == 'noun':
        plural_form = input(f"Enter the plural form of '{word}': ")
        singular_form = input(f"Enter the singular form of '{word}': ")
    elif part_of_speech == 'verb':
        tense = input(f"Enter a common tense for '{word}' (e.g., past, present, future): ")
        plural_form = singular_form = ""  # Not applicable for verbs
    elif part_of_speech == 'adjective':
        comparative_form = input(f"Enter the comparative form of '{word}': ")
        superlative_form = input(f"Enter the superlative form of '{word}': ")
        plural_form = singular_form = ""  # Not applicable for adjectives
    elif part_of_speech == 'adverb':
        degree = input(f"Enter a degree for '{word}' (e.g., more, most): ")
        plural_form = singular_form = ""  # Not applicable for adverbs

    sentence = input(f"Enter a sentence using '{word}': ")

    dictionary[word] = {
        'Meaning': meaning,
        'Part of Speech': part_of_speech,
        'Plural Form': plural_form,
        'Singular Form': singular_form,
        'Sentence': sentence
    }
    
    if part_of_speech == 'adjective':
        dictionary[word]['Comparative Form'] = comparative_form
        dictionary[word]['Superlative Form'] = superlative_form
    elif part_of_speech == 'verb':
        dictionary[word]['Tense'] = tense
    elif part_of_speech == 'adverb':
        dictionary[word]['Degree'] = degree

    print(f"'{word}' added to the dictionary.")

# Function to delete a word
def delete_word(dictionary):
    word = input("Enter the word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"'{word}' has been deleted from the dictionary.")
    else:
        print(f"'{word}' not found in the dictionary.")

# Function to edit a word's details
def edit_word(dictionary):
    word = input("Enter the word to edit: ")
    if word in dictionary:
        meaning = input(f"Enter the new meaning of '{word}': ")

        # Validate the part of speech
        while True:
            part_of_speech = input(f"Enter the new part of speech for '{word}': ").lower()
            if part_of_speech in valid_parts_of_speech:
                break
            else:
                print("Error: Invalid part of speech. Please enter one of the following:")
                print(", ".join(valid_parts_of_speech))

        # Additional prompts based on part of speech
        if part_of_speech == 'noun':
            plural_form = input(f"Enter the new plural form of '{word}': ")
            singular_form = input(f"Enter the new singular form of '{word}': ")
        elif part_of_speech == 'verb':
            tense = input(f"Enter a common tense for '{word}' (e.g., past, present, future): ")
            plural_form = singular_form = ""  # Not applicable for verbs
        elif part_of_speech == 'adjective':
            comparative_form = input(f"Enter the new comparative form of '{word}': ")
            superlative_form = input(f"Enter the new superlative form of '{word}': ")
            plural_form = singular_form = ""  # Not applicable for adjectives
        elif part_of_speech == 'adverb':
            degree = input(f"Enter a new degree for '{word}' (e.g., more, most): ")
            plural_form = singular_form = ""  # Not applicable for adverbs

        sentence = input(f"Enter the new sentence using '{word}': ")

        dictionary[word] = {
            'Meaning': meaning,
            'Part of Speech': part_of_speech,
            'Plural Form': plural_form,
            'Singular Form': singular_form,
            'Sentence': sentence
        }

        if part_of_speech == 'adjective':
            dictionary[word]['Comparative Form'] = comparative_form
            dictionary[word]['Superlative Form'] = superlative_form
        elif part_of_speech == 'verb':
            dictionary[word]['Tense'] = tense
        elif part_of_speech == 'adverb':
            dictionary[word]['Degree'] = degree

        print(f"'{word}' has been updated.")
    else:
        print(f"'{word}' not found in the dictionary.")

# Function to display all words (sorted alphabetically)
def display_all_words(dictionary):
    index = 1
    if not dictionary:
        print("The dictionary is empty.")
    else:
        print("\n--- Word Dictionary ---")
        for word in sorted(dictionary.keys()):
           
            print(f"\n({index})")
            print(f"{word} - {dictionary[word]['Meaning']} ({dictionary[word]['Part of Speech']})")
            if dictionary[word]['Part of Speech'] == 'noun':
                print(f"Plural Form: {dictionary[word]['Plural Form']}")
                print(f"Singular Form: {dictionary[word]['Singular Form']}")
            elif dictionary[word]['Part of Speech'] == 'adjective':
                print(f"Comparative Form: {dictionary[word].get('Comparative Form', '')}")
                print(f"Superlative Form: {dictionary[word].get('Superlative Form', '')}")
            elif dictionary[word]['Part of Speech'] == 'verb':
                print(f"Tense: {dictionary[word].get('Tense', '')}")
                
            print(f"Sentence: {dictionary[word]['Sentence']}\n")
            index += 1  

# Function to search for a word
def search_word(dictionary):
    word = input("Enter the word to search: ")
    if word in dictionary:
        print(f"\n{word} - {dictionary[word]['Meaning']} ({dictionary[word]['Part of Speech']})")
        
        if dictionary[word]['Part of Speech'] == 'noun':
            print(f"Plural Form: {dictionary[word]['Plural Form']}")
            print(f"Singular Form: {dictionary[word]['Singular Form']}")
            
        elif dictionary[word]['Part of Speech'] == 'adjective':
            print(f"Comparative Form: {dictionary[word].get('Comparative Form', '')}")
            print(f"Superlative Form: {dictionary[word].get('Superlative Form', '')}")
            
        elif dictionary[word]['Part of Speech'] == 'verb':
            print(f"Tense: {dictionary[word].get('Tense', '')}")
        
        print(f"Sentence: {dictionary[word]['Sentence']}\n")
    else:
        print(f"'{word}' not found in the dictionary.")

# Main menu
def menu():
    print("\n--- Word Dictionary Menu ---")
    print("1. Add word")
    print("2. Delete word")
    print("3. Edit word")
    print("4. Display all words (sorted)")
    print("5. Search word")
    print("6. Exit")

# Main loop using imported dictionary
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_word(dictionary)
    elif choice == '2':
        delete_word(dictionary)
    elif choice == '3':
        edit_word(dictionary)
    elif choice == '4':
        display_all_words(dictionary)
    elif choice == '5':
        search_word(dictionary)
    elif choice == '6':
        print("Exiting the Word Dictionary.")
        break
    else:
       print("Invalid choice, please try again.")