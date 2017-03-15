def countdown(n):
    print(n)
    countdown(n - 1)


def countdown(n):
    'counts down to 0'
    if n <= 0:
        print('Blastoff!!!')
    else:
        print(n)
        countdown(n - 1)


def vertical(n):

    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)
        print(n % 10)
