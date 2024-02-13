def add(a: int, b: int, *args):
    my_sum = a + b
    for i in args:
        my_sum = my_sum + i
    return my_sum


def using_keyword_args(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def using_default_values(a: int, b: int, c=10):
    print("\nsum result", a + b + c)


if __name__ == '__main__':
    print("sum=", add(a=3, b=4))
    print("multiple args sum = ", add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    print("\nvalues with keyword args")
    using_keyword_args("a", "b", name="Adrian", grade="ML")

    #unpacking
    my_list = {
        "name": "Adrian",
        "grade": "ML",
        "location": "Cluj",
    }
    print("\n results with unpacking")
    using_keyword_args("a", "b", **my_list)

    using_default_values(a=1, b=2)
    using_default_values(a=1, b=2, c=3)
