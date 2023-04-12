#password generator
import random

no_of_alphabets = int(input("Enter the number of alphabets you want in your password: "))
no_of_numbers = int(input("Enter the number of number you want  in your password: "))
no_of_special_characters = int(input("Enter minimum number of special character you want: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#52 letters
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_characters = ['!','@','#','$','%','^','&','*','`','?','-','+','/']  #13

total_characters = no_of_alphabets + no_of_numbers + no_of_special_characters
password = ""
num = 1
while  no_of_alphabets + no_of_numbers + no_of_special_characters > 0:
    roll =  random.randint(0,2)
    if roll == 0 and no_of_alphabets != 0:
        password += letters[random.randint(0,51)]
        no_of_alphabets = no_of_alphabets-1
    elif roll == 1 and no_of_numbers !=0:
        password += numbers[random.randint(0,9)]
        no_of_numbers = no_of_numbers-1
    elif roll == 2 and no_of_special_characters !=0:
        password += special_characters[random.randint(0,12)]
        no_of_special_characters = no_of_special_characters-1

print(f"Your password is {password}")

    