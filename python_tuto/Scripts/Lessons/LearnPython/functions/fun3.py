def outer():
    n = 5

    def inner():
        nonlocal n  # this line is optional
        n = 25
        print(n)

    inner()  # n = 25
    print(n)  # n = 5


outer()
