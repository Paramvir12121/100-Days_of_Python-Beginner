#Calculator app

end_flag = False


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b


refer_dict = {'+':add, '-':subtract, '*':multiply, '/':divide}


num1 = int(input("Enter first number: "))

for key in refer_dict:
    print(key)
operation_symbol = input("Enter operation symbol out of the above symbols: ")

num2 = int(input("Enter second number: "))





for key in refer_dict:
    if key==operation_symbol:
        calc_func = refer_dict[key]
        output_val = calc_func(num1,num2)
        print(f"{num1} {key} {num2} = {output_val}")


# while end_flag == False:
#     operation = input("Which operation would you like to perform: +\n-\n*\n/\n")
#     if operation == '+':
#         add(num1,num2)
#     elif operation=='-':
#         subtract(num1,num2)
#     elif operation=='*':
#         multiply(num1,num2)
#     elif operation=='':
#         divide(num1,num2)
#     else:
#         print("Invalid input!")

#     check = input("To exit, type 'exit': ")
#     if check == 'exit':
#         end_flag = True