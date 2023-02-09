#Tip Percentage calculator
billAmount = input("What is the bill? $")
tipPercentage = input("What amount of bill you want to tip? 10,12 or 15 ")
fullBill= float(billAmount) + (float(billAmount) * (float(tipPercentage) /100))
print(f"Your final bill is {round(fullBill,2)} dollers.")
numOfPeople = input("Among how many people you want to divide it? ")
finalBill = fullBill/float(numOfPeople)
print(f"The final bill per person is {round(finalBill,2)} dollers")


