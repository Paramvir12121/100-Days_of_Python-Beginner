import random

#selected a randdom word from list
word_list = ['apple', 'banana', 'cherry', 'dog', 'cat', 'bird', 'desk', 'chair', 'book', 'car', 'bus', 'house', 'tree', 'sun', 'moon', 'star', 'water', 'fire', 'earth', 'wind', 'snow', 'ice', 'beach', 'mountain', 'river', 'ocean', 'lake', 'music', 'art', 'painting', 'history', 'math', 'science', 'language', 'culture', 'food', 'drink']

word_list_len = len(word_list)
word_choice = word_list[random.randint(0,word_list_len-1)]
#print(f"word chosen is {word_choice}")
word_choice_len = len(word_choice)
hangman_display = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman_display_index = 0

word_choice = list(word_choice)
# print("Word Choice",word_choice)
view_list = []
num = 0
while num < word_choice_len:
    num += 1
    view_list.append('_')
print(view_list)
full_flag = True

while full_flag==True:
    full_flag = False
    match_flag = False
    win_flag = True
    letter = input("Enter your guess letter: ").lower()
    #inputed letter is matched against the letters in chosen word
    position = 0
    for i in word_choice:
        if i==letter:
            #print("match")
            match_flag=True
            view_list[position]=letter
            word_choice[position] = "_"
        #else:
            #print("No Match")
        position += 1
    if match_flag ==False:
        hangman_display_index += 1

    for x in view_list:
        if x == "_":
            full_flag=True
    

    print(view_list)
    print(hangman_display[hangman_display_index])
    if hangman_display_index > 5:
        print("The word was ",word_choice)
        print("You lose")
        break

    for x in view_list:
        if x == "_":
            win_flag=False
    if win_flag == True:
        print("You WIN!!!")

    

