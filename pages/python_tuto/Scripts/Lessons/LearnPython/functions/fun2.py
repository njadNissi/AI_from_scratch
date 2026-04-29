
# def sum(*numbers):
#     print('numbers are: ')
#     for n in numbers:
#         print(n)


# sum(1, 9, -5, 7)


def get_message():
    return "Hello John"


message = get_message()
# print(message)
# print(get_message())


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b


do_operation(5, 4, sum)
do_operation(5, 4, multiply)


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply


do_operation(5, 4, select_operation(2))
