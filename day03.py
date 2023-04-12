#adventure game

fail="HAHAHA you lose traveller!! you lose!!!!"

print("Welcome Weary traveller! Welcome to Treasure Island ")

forkChoice = input("You walk on a the road and reach a forked path. You can go left or right. Which do you choose??\n")
if forkChoice == 'left':
    print("You choose well traveller!")
    swimChoice = input("You reach river.Do you wait or swim?\n")
    if swimChoice =='wait':
        print("You wait and a boat arrives. You walk on the deck and on it you have three doors; red, yellow and blue.")
        doorChoice = input("Which Door doyou choose?\n")
        if doorChoice=='yellow':
            print("Damn, you found the Treasure \n")
            print('''  
                       _________________
                      |                 |
                      |______<>o<>______|
                      |-----------------|
                      |-----------------|
                      |_________________|  
                      ''')
        else:
            print(fail)
    else:
        print(fail)

else:
    print(fail)
