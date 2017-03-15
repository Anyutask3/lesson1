# employee = {
#     '864-20': ['Arm', 'Spartyan'],
#     '987-65': ['Vlad', 'Tundyan'],
#     '100-01': ['Kiazh', 'Damyan']}
# print(type(employee))
# print(employee['864-20'][0])

# days = {'Mo': 1, 'Tu': 2, 'W': 3}
#
# days2 = {'Tu': 2, 'Fr': 5}
# # print(days.pop('Tu'))
# # print(days)
# # days['Tu']=2
# # print(days)
# days.update(days2)
# # print(days.items())
# # print(days.keys())
# # print(days.values())
# for k,v in days.items():
#     print(k,v)

#
# # def frequency(itemList):
# itemList = [95, 96, 100, 85, 95, 90, 95, 100, 100]
# counters = {}
# for item in itemList:
#     if item in counters:  # increment item counter
#         counters[item] += 1
#     else:  # create item counter
#         counters[item] = 1
# # return counters
# print(counters)

# def lst(x):
# # itemList2 = x.split()
# # print(itemList2)
#     counters = {}
#     for item in x.split():
#         if item in counters:
#             counters[item] += 1
#         else:
#             counters[item] = 1
#     print(counters)
#     # return list
# # lst('to be or not to be')
# def lokup():
#     phonebook = {
#         'Arm':'56-78-90',
#         'Vlad':'34-56-78',
#         'Kiazh':'48-76-54'}
#     while True:
#         print('Enter your name ', end='')
#         name=input()
#         if name in phonebook:
#             print(phonebook[name])
#         else name =='':
#             break
# lokup()

# # sorting list of tuples
t = [('a', 10), ('c', 22), ('b', 1)]
# # t.sort()
# # print(t)
# x=sorted(t)
# print(x)

# lst=lst()
# d = {'a':10, 'b':1, 'c':22}
# for k,v in d.items():
#     lst.append((v,k))
# print(list)
# sorted_lst=sorted(lst, reverse=True)
# print(sorted_lst)

f=open('romeo.txt', 'r')
s = f.read().lower()
# itemList = s.split()
# # print(itemList)
counters={}
for item in s.split():
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
# print(counters)
lst=list()
for k,v in counters.items():
    lst.append((v,k))
print(lst)
sorted_lst=sorted(lst, reverse=True)
print(sorted_lst)

