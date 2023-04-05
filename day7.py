import random

#selected a randdom word from list
word_list = ['because', 'therefore', 'baboon', 'ardwark']
word_list_len = len(word_list)
word_choice = word_list[random.randint(0,word_list_len-1)]
print(f"word chosen is {word_choice}")
word_choice_len = len(word_choice)

letter = input("Enter your guess letter: ").lower()
#inputed letter is matched against the letters in chosen word
position = 0
positions = []
for i in word_choice:
    if i==letter:
        print("match")
        positions.append(position)
    else:
        print("No Match")
    position += 1

print("positions :",positions)

def view_word(word_list_len,letter,positions):
    view_list = []
    num = 0
    while num < word_list_len:
        num += 1
        view_list.append('_')
    print(view_list)
    


print("world len list:",word_list_len)
view_word(word_choice_len,letter,positions)
