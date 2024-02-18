# Arguments *args
- To allow any number of arguments in the function:
```
def add(*args):
    num = 0
    for n in args:
        num = num + n
    return num
```
- We can have any number of arguments in the above function.
- args notation is not strictly necessariry by * is.
- args stors the variables in form of a tuple.