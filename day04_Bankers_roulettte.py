import random

banker_list = []

print("Who is at the table?")

while True:
    banker = input("Enter Participant's name or type end to get payee: ")
    if banker == "end":
        break
    banker_list += [banker]

number_of_bankers = int(len(banker_list))

paying_banker = banker_list[random.randint(0, number_of_bankers - 1)]

print(f"{paying_banker} is paying for the bill.")
