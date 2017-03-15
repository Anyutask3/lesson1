""""Some Documetion
This is my firt full project
"""

import countdown


def summa(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + summa(numList[1:])


print(summa([1, 3, 5, 7, 9]))


def main():
    print(__name__)
    countdown.countdown(5)
    countdown.vertical(3145)


if __name__ == '__main__':
    main()
