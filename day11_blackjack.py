import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# User get cards
user = []
user.append(random.choice(cards))
user.append(random.choice(cards))
print("User cards: ",user)

#dealer get cards
dealer = []
dealer.append(random.choice(cards))
dealer.append(random.choice(cards))
print("computer cards: ",dealer)

# user = [1,11]
# dealer = [10,5]
while True:
    print("Dealer has ",dealer[0])
    print("You have", user)
    #does the user or computer has blackjack?
    usersum = 0
    dealersum = 0
    for i in user:
        usersum += i
    for x in dealer:
        dealersum += x
    print("usersum is ",usersum,"dealersum is ",dealersum)
    if usersum == 21 and dealersum == 21:
        print("Blackjack!!! But it is a Draw")
        break
    if usersum == 21:
        print("Blackjack!!! You Win")
        break
    if dealersum == 21:
        print("Blackjack!!! You lose :(")
        break
    usersum = 0
    dealersum = 0
    for i in user:
        usersum += i
    for x in dealer:
        dealersum += x
   #is user score over 21?
    if usersum>21:
        #does user has ace?
        for x in user:
            if x == 11:
                print("Yes, user has ace!")
                user.remove(11)
                user.append(1)
         #is user score still over 21?
        if usersum>21:
            print(f"Your score is {usersum} and your cards are {user}")
            print("You Lose")
            break
    #ask user to ddraw another cards
    choice = input("Would you like to draw another card? Enter 'd' to draw or enter to continue.")
    if choice == 'd':
        user.append(random.choice(cards))
    else: 
        print("Dealer's Turn")

        #check if score is less than 16
        if dealersum<16:
            dealer.append(random.choice(cards))
        dealersum = 0
        for x in dealer:
                dealersum += x
        print(f"Dealer score is {dealersum} and your cards are {dealer}")
        if dealersum>21:
            print("You Win")
        #Compare Scores
        if usersum>dealersum:
            print("You Win!!!")
        elif usersum<dealersum:
            print("You lose :(")    
        else:
            print("It's a draw")