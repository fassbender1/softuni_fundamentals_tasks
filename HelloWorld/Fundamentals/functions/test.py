# passwd = input()
#
# print(len(passwd))
#
# if len(passwd) < 6 or len(passwd) > 10:
#     print(f"more than 10 or less than 6 chars")
#
# def tricky_function():
#     return [lambda x: x * i for i in range(5)]
#
#
# results = [m(2) for m in tricky_function()]
# print(results)

def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x = 10

    inner_function()
    return x


print(outer_function())
