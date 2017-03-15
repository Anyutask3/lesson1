# def f(b):  # f has global scope, b has local scope
#     a = 6  # a has scope local to function call f()
#     return a * b  # this a is the local a
#
#
# a = 0  # this a has global scope
# print('f(3) = {}'.format(f(3)))
# print('a is {}'.format(a))  # global a is still 0
a = 0
#
# def f(b):  # f : global scope, b : local scope
#     global a
#     a = 6  # a : local scope
#     return a * b
#
# print(f(5))
#
# print(a)
