import random

#selected a randdom word from list
word_list = ['because', 'therefore', 'baboon', 'ardwark']
word_list_len = len(word_list)
word_choice = word_list[random.randint(0,word_list_len-1)]
print(f"word chosen is {word_choice}")
word_choice_len = len(word_choice)

letter = input("Enter your guess letter: ").lower()

#to create a a list of _ corresponding to choesn letter
view_list = []
num = 0
while num < word_choice_len:
    num += 1
    view_list.append('_')
print(view_list)


#inputed letter is matched against the letters in chosen word
position = 0
positions = []
for i in word_choice:
    if i==letter:
        print("match")
        view_list[position]=letter 
    else:
        print("No Match")
    position += 1


print(view_list)
 

