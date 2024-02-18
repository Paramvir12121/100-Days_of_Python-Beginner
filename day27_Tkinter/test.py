# def add(*args):
#     num = 0
#     for n in args:
#         num = num + n
#     return num

# print(add(1,2,3))

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)