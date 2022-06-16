import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
data_dict = {value.letter: value.code for (key, value) in data.iterrows()}

user_input = list(input("Enter a word : ").upper())
print(user_input)
result = [data_dict[data] for data in user_input]

print(result)
