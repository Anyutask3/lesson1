# def read_write():
#     x1=open('tobe.txt', 'w')
#     x1.write('to be vhjf,  wejhrfksdgmv')
#     x1.close()
#
#     x2 = open('tobe.txt','r')
#     y = x2.read()
#     x2.close()
#     print(y)
#
#
# read_write()
def histogram(a):
    x1 = open('tobe2.txt', 'w')
    for i in a:
        x1.write('*'*i+ '\n')
    x1.close()

histogram([4,7,9])
