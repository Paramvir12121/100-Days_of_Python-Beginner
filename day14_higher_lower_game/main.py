from game_data import data
from art import logo, vs
import random

user_list = []
user_list = data
score = 0
print(logo)

def get_random(list):
    random_element = random.choice(list)
    list.remove(random_element)
    return random_element

##select the first value
first_value = get_random(user_list)
print(first_value['name'])
print(f"{first_value['name']} is {first_value['description']} from {first_value['country']}.")
while True:
    print(vs)
    result= False
    ##select the second 
    second_value = get_random(user_list)
    print(second_value['name'])
    print(f"{second_value['name']} is {second_value['description']} from {second_value['country']}.")
    #does first have higher followers than second?
    choice = input(f"\nIf you believe {first_value['name']} have Higher number of followers than {second_value['name']},Enter Y, if not enter N\n")
    choice = choice.lower()
    firsts_followers = first_value['follower_count'] 
    seconds_followers = second_value['follower_count']
    if firsts_followers> seconds_followers and choice=='y' or firsts_followers< seconds_followers and choice=='n':
        result = True
        score += 1
        print("You are correct!!!")
        print(f"{first_value['name']} has {first_value['follower_count']} Million followers.")
        print(f"{second_value['name']} has {second_value['follower_count']} Million followers.")
        print("Your score is ",score,"\n\n\n")
        if firsts_followers < seconds_followers:
            first_value = second_value
        print(first_value['name'])
        print(f"{first_value['name']} is {first_value['description']} from {first_value['country']}.")
    else:
        result = False
        print("Not Correct!!!")
        print(f"{first_value['name']} has {first_value['follower_count']} Million followers.")
        print(f"{second_value['name']} has {second_value['follower_count']} Million followers.")
        print("You Lose!!!\nYour score is",score)
        break
    