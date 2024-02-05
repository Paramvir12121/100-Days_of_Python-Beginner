import pandas

df = pandas.read_csv("alphabet_conversion.csv")

# print(df)

# Creating a dict with key as letters and values are letters 

dict = {row.letter:row.code for (index,row) in df.iterrows()}

print(dict)


def find_letter(letter):
    for (key,val) in dict.items():
        if key == letter:
            print(val)
            return val
    


input_word = input("Enter a word: ").upper()

input_word = list(input_word)

nato_code = [find_letter(letter) for letter in input_word]

print(nato_code)



