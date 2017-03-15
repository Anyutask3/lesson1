# while True:
#         nums = input('Enter 2 digits (format: x y):')
#         if nums ==''
#             break
#         try:
#             (x, y) = nums.split()
#             x = int(x)
#             y = int(y)
#             res = x/y
#             print(res)
#         except ZeroDivisionError:
#             print('ZeroDivisionError')
#             print('try again without 0')
#         except ValueError:
#             print('ValueError')
#             print('try again without letters')
#         except:
#             print("Something went wrong!")
#             raise
# #
#
# def read_data(filename):
#     lines = []
#     infile = None
#     try:
#         with  open(filename, encoding="utf8") as infile:
#             for line in infile:
#                 lines.append(line)
#     except (IOError, OSError) as err:
#         print(err)
#         return []
#     finally:
#         if infile is not None:
#             infile.close()
#     return lines
# a=read_data('fifteen.txt')
# print(a)