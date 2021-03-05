# scope_test()
x = 5


def scope_test():
    print(x)
    print(x+5)
    # x += 5


# scope_test()

# *args : multiple parameters


def args_test(*args):
    print(type(args))
    print(args)
    for arg in args:
        print(arg)


# args_test(1, 2, 3, 4)
# args_test(list(range(4)))

# **kawargs : keyword arguments


def kwarg_test(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for item in kwargs.items():
        print(item)


# kwarg_test(a=1, b='hi')
kwarg_test(x=[1,2,3], y='Hello')
