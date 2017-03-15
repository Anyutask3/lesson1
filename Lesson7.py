# from gpcharts import figure
#
# #simple line graph, as described in the readme.
# fig1 = figure()
# fig1.plot([8,7,6,5,4])
#
# #another line graph, but with two data types. Also adding title
# fig2 = figure(title='Two lines',xlabel='Days',ylabel='Count',height=600,width=600)
# xVals = ['Mon','Tues','Wed','Thurs','Fri']
# yVals = [[5,4],[8,7],[4,8],[10,10],[3,12]]
# fig2.plot(xVals,yVals)

import random
# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# print(squares)

# squares = [x**2 for x in range(10) if x>4]
#
# # print(squares)
# # lst=[(x, x**2, x**3) for x in range(6)]
# # print(lst)
# z = sum([x for  x in range(1,101) if x%2==0])
# print(z)
import requests
x = requests.get('http://news.am/arm')
start=1329
end=1423
for symbol in x:
    print(symbol, ord(symbol))
#
# for i in range(start, end + 1):
#     print(format(i, 'X'), end=' ')  #hex
#     print(i, end=' ')               #dec
#     print(chr(i))              #letter

# x = requests.get('http://news.am/')
# print(x.text)





