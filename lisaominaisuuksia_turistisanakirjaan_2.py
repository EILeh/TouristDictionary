"""

Tourist dictionary

Program is a simple dictionary to help a tourist while abroad. The dictionary
can translate wanted word when user inputs W, add a new word to be translated by
inputting A, removes a word from the dictionary with command R, prints all
the words in the dictionary with command P, translates an entire sentence
when inputting T and program ends when inputting Q. If the word in the
translated sentence is not in the dictionary, the word in question is printed to
the sentence in English.

Writer of the program: EILeh
"""

def main():

    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")

    # Dictionary sorted.
    sorted_content = sorted(english_spanish)

    # Dictionary content separated by comma.
    content = ", ".join(sorted_content)
    print(content)

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")

            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "A":

            added_word_in_english = input\
                ("Give the word to be added in English: ")

            added_word_in_spanish = input\
                ("Give the word to be added in Spanish: ")

            # New key-value pair.
            update_dictionary = {added_word_in_english: added_word_in_spanish}

            # New dictionary is created by updating the old one.
            new_dictionary = english_spanish.update(update_dictionary)

            print("Dictionary contents:")
            sorted_content = sorted(english_spanish)
            content = ", ".join(sorted_content)
            print(content)

        elif command == "R":

            remove_word = input("Give the word to be removed: ")

            # If word is not in dictionary, it can't be removed from it.
            if remove_word not in english_spanish:
                print("The word", remove_word, "could not be found from "
                                               "the dictionary.")

            # Removes the word from the dictionary by removing the key-value
            # pair.
            else:
                del english_spanish[remove_word]

        elif command == "P":

            print()
            print("English-Spanish")

            # Goes through the sorted dictionary a word by word and prints
            # the entire dictionary.
            for sorted_dictionary_english in sorted(english_spanish):
                print(f"{sorted_dictionary_english} "
                      f"{english_spanish[sorted_dictionary_english]}")

            print()

            # Function takes one parameter key and returns the value from the
            # certain key.
            def spanish(key):
                return english_spanish[key]

            print("Spanish-English")

            # Goes through the sorted dictionary where the value is gotten from
            # the function spanish.
            for sorted_dictionary_spanish in sorted(english_spanish,
                                                    key=spanish):
                print(f"{english_spanish[sorted_dictionary_spanish]} "
                      f"{sorted_dictionary_spanish}")

            print()

        elif command == "T":

            text_to_be_translated = input\
                ("Enter the text to be translated into Spanish: ")

            split_input = text_to_be_translated.split(" ")
            length_of_the_split_input = len(split_input)

            print(f"The text, translated by the dictionary:")

            is_translation_in_progress = True

            i = 0

            while is_translation_in_progress:
                # Key in english_spanish.
                for key in english_spanish:
                    # If i is greater than the variable
                    # length_of_the_split_input minus 1, there is nothing to
                    # translate.
                    if i > length_of_the_split_input - 1:
                        break

                    # If split_input at index i is found in english_spanish,
                    # the word is translated.
                    elif split_input[i] in english_spanish:
                        print(english_spanish.get(split_input[i]), " ", sep="",
                              end="")

                    # If the split_input at index i is not found in
                    # english_spanish, the word is printed as it is.
                    else:
                        print(split_input[i], " ", sep="", end="")

                    # The variable i grown by one to keep count of the
                    # current word.
                    i += 1

                # If i is less than the variable length_of_the_split_input,
                # then there is more words to be translated and loop is
                # continued again.
                if i < length_of_the_split_input:
                    continue

                # If all the words have been translated, the variable
                # is_translation_in_progress gets a value False.
                else:
                    is_translation_in_progress = False

            print("")

        elif command == "Q":

            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
