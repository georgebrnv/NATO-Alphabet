import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_data)

nato_alphabet_dic = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    users_input = input("Type in your word: ").upper()
    try:
        nato_input_list = [nato_alphabet_dic[letter] for letter in users_input]
    except KeyError:
        print("Only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_input_list)


generate_phonetic()