def add(*args):
    num = 0
    for n in args:
        num = num + n
    return num

print(add(1,2,3))