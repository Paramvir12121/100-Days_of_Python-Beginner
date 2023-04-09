n = int(input("Enter your number: "))
'''Dear Alexandru,

I am writing to request a leave of absence from May 23, 2023, to June 24, 2023 due to my travel plans outside the country. 

Could you please let me know what processes I need to follow to make sure that my leave request is properly documented and approved? Also, please let me know if there are any additional steps, I need to take to ensure a smooth transition during my absence.

I understand that my absence may cause some inconvenience, and I apologize for any inconvenience caused. 

Sincerely, 
Paramvir Singh
'''


def prime_checker(n):
    primeflag = True
    checker_no = 2
    for i in range(2, n):
        print("checker no", checker_no)
        diff = n % checker_no
        checker_no += 1
        if diff == 0:
            print("diff ", diff)
            primeflag = False
            break

    if primeflag == True:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is a NOT Prime Number.")


prime_checker(n)
