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

end_flag = False
num1 = int(input("Enter first number: "))
num2 = 0

for key in refer_dict:
    print(key)
operation_symbol = input("Enter operation symbol out of the above symbols: ")

num2 = int(input("Enter next number: "))

# num2 = int(input("Enter next number: "))
# for key in refer_dict:
#     if key==operation_symbol:
#         calc_func = refer_dict[key]
#         output_val = calc_func(num1,num2)
#         print(f"{num1} {key} {num2} = {output_val}")


while end_flag == False:
    for key in refer_dict:
        if key==operation_symbol:
            calc_func = refer_dict[key]
            output = calc_func(num1,num2)
            print(f"{num1} {key} {num2} = {output}")
            num1 = output
    if input("Press 'n' to exit, any other key to continue: ") == 'n':
        end_flag == True
        break
    else:
        num2 = int(input("Enter next number: "))
        for key in refer_dict:
            print(key)
        operation_symbol = input("Enter operation symbol out of the above symbols: ")

        


