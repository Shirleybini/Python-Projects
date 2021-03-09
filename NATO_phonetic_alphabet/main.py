import pandas as pd
Nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame

nato = {row.letter:row.code for (index,row) in Nato_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ")
name_letters = list(name)

try:
    code = [nato[letter.upper()] for letter in name_letters]
    print(code)

except KeyError:
    print("Sorry only leters in the alphabet please.")