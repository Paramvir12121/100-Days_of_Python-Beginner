numbers = [1,2,3]

## With for loop
# new_list =[]
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

## Whith list comprehension
new_list = [n+1 for n in numbers]

print(new_list)


## For string

name = "Paramvir"
name_list = [n for n in name]
print(name_list)


## for looping function
range_list = [n*2 for n in range(1,5)]
print(range_list)

## We can add conditional statemetns
names = ["Harry", "Alex","James","Beth"]
short_names = [name for name in names if len(name)<5]
capitol_long_names = [name.upper() for name in names if len(name)> 4]
print(short_names)
print(capitol_long_names)
