# def cities3():
#     lst = []
#     while True:
#         city = input(
# 		'Enter city: ')
#
#         if city == '':
#             break
#
#         lst.append(city)
#     print(lst)
#     # return lst
# cities3()


def before(table):
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num,end=' ')

print(before([
  [2, 3, 0, 6],
  [0, 3, 4, 5],
  [4, 5, 6, 0]
]))


























# lst=[3,1,-7,-4,9,-2]
# def negativ(lst):
#     for i in range(len(lst)):
#         if lst[i]<0:
#             return i
#     return None
#     return lst
# print(negativ(lst))


# p=1
# c=1
# while c<=15:
#     p,c=c,p+c
# return c


# def hell():
#     with True:
#         name=input('What is your name?')

# def cities():
#     lst=[]
#     with True:
#     city=input("enter your name")
#
#
#

