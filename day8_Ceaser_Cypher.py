# today we make a ceaser sypher that shifts the user data by a certain number of digits

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = ''


def encrypt(shift):
    message = input("Enter your mesage: ").lower()
    message_list = list(message)
    # print("message_list: ", message_list)
    code_list = []
    code = ''
    for x in message_list:
        alphabet_index = alphabets.index(x)
        # print("alphabet_index", alphabet_index)
        if alphabet_index + shift > len(alphabets):
            alphabet_index = shift - (len(alphabets) - alphabet_index)
        else:
            alphabet_index = alphabet_index + shift
        # print("new alphabet_index", alphabet_index)
        code_list.append(alphabets[alphabet_index])
    # print("code list is: ", code_list)
    for x in code_list:
        code = code + x
    print("Final Code is : ", code)


def decrypt(shift):
    code = input("Enter your code: ").lower()
    code_list = list(code)
    # print("code_list: ", code_list)
    message_list = []
    message = ''
    for x in code_list:
        alphabet_index = alphabets.index(x)
        # print("alphabet_index", alphabet_index)
        if alphabet_index - shift < 0:
            alphabet_index = len(alphabets) - (shift - alphabet_index)
        else:
            alphabet_index = alphabet_index - shift
        # print("new alphabet_index", alphabet_index)
        message_list.append(alphabets[alphabet_index])
    # print("code list is: ", message_list)
    for x in message_list:
        message = message + x
    print("The message is : ", message)


while end != 'yes':
    direction = input(
        "Type 'encode' to encrypt and type 'decode' to decrypt: ")
    while True:
        try:
            shift = int(input("Type the shift number: "))
            break
        except:
            print("Invalid input, try again!")

    if direction == 'encode':
        encrypt(shift)
    elif direction == 'decode':
        decrypt(shift)
    else:
        print('Invalid input, try again.')
    end = input(
        "Would you like to exit?  Press enter to continue or enter 'yes to exit. ")
