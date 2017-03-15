


# def countdown(n):
#     if n <= 0:
#         print("Stop")
#     else:
#         print(n)
#         countdown(n - 1)
# # countdown(5)

def vertical(n):

    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)
        print(n % 10)


# n!=n*(n-1)! if n>0
# 0!=1

# def factorial(n):
#     if n<=0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))

def Hurray(n):
    if n==0:
         print("Stom somting is wrong")
    else:
        print(" Hip ", end='')
        Hurray(n-1)
Hurray(5)
if __name__ == '__main__':
    Hurray(5)
    vertical(3154)