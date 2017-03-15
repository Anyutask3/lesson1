#
# try:
#     strAge = input('Enter your age: ')
#     intAge = int(strAge)
#     print('You are {} years old.'.format(intAge))
# except NameError as e:
#     print(e)
# except ValueError as e:
#     print("ghdsfhyf")
#     print(e)
# 
# def readAge(filename):
#     'converts first line of file filename to an integer and prints it'
#     try:
#         infile = open(filename)
#         strAge = infile.readline()
#         age = int(strAge)
#         print('age is', age)
#     except ValueError:
#         print('Value cannot be converted to integer.')
#     # except IOError as e:
#     #     print('JHGJHGJHM', e)
#     except:
#         raise
#
# readAge('fifteen2.txt')