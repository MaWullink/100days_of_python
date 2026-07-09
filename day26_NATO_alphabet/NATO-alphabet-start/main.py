import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {}

for (index, row) in data.iterrows():
    dictionary[row.letter] = row.code

while True:
    try:
        user_input = input("Type a word to convert into NATO phonetic code: ").upper().strip()
        letters = list(user_input)
        nato_list = [dictionary[letter] for letter in letters]
        print(nato_list)
    except KeyError:
        print("We only accept words.")


