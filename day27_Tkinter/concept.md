# Arguments *args
- In arguments, you refer variables added in function by position.

- We can have any number of arguments in the above function.
- args notation is not strictly necessariry by * is.
- args stors the variables in form of a tuple.
- To allow any number of arguments in the function:
```
def add(*args):
    num = 0
    for n in args:
        num = num + n
    return num
```

# Key Word Arguments **kwargs
- To allow any number of arguments in the function:
- In arguments, you refer variables added in function by key name.
```
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)  # {'add': 3, 'multiply': 5}
```