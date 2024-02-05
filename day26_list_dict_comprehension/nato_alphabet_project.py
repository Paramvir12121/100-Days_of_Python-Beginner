import pandas

df = pandas.read_csv("alphabet_conversion.csv")

# print(df)

# Creating a dict with key as letters and values are letters 

dict = {row.letter:row.code for (index,row) in df.iterrows()}

print(dict)
    

input_word = input("Enter a word: ").upper()

input_word = list(input_word)

nato_code = [dict[letter] for letter in input_word]

print(nato_code)



