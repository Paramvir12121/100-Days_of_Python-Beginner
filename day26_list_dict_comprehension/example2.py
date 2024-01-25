
list_of_strings = input("Enter a long number with commas: ").split(',')

print(list_of_strings)

result = [int(n) for n in list_of_strings if (int(n)%2)==0]

print(result)