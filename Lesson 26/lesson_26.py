import pandas

# Importing CSV file with pandas
nato_alphabet = pandas.read_csv('lesson 26/nato_phonetic_alphabet.csv')

# Creating an dict with the csv file, using pandas functions and list comprehension
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def generate_phonetic():

    # Taking the input to make the conversion
    user_word = input("Type a word to change to NATO format:\n").upper()

    try:
        # Making the conversion using the word as key search in nato_dict
        splited_user_word = [nato_dict[word] for word in user_word]
    except KeyError:
        print("Only use words in Alphabet")
        generate_phonetic()
    else:
        # Showing the result
        print(splited_user_word)


generate_phonetic()
