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

n = int(input("Enter your number: "))

prime_checker(n)
