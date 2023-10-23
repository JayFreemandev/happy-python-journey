def add(a, b):
    return a + b

print(add(1,2))

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,))

def print_kwargs(**kawargs):
    print(kwargs)
