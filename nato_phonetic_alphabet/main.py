import pandas

name = input("Input your message: ").upper()
data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = [row.code for j in name for (index, row) in data_nato.iterrows() if row.letter == j]
print(nato)
