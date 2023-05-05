#Question - 1

# tup = (1,2,'Trijal')
#
# print(tup.index('Trijal'))


#Question-2

# list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
#
# # Use the zip() function to unzip the list of tuples
# unzipped_list = list(zip(*list_of_tuples))
#
# print(list(unzipped_list))


#Question-3


# list_of_tuples = [(), (),('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#
# ans = [t for t in list_of_tuples if t]
#
# print(ans)

#Question-4

# grades = {'Alice': 90, 'Bob': 85, 'Charlie': 95, 'David': 80}
# key = 'Bob'
# flag = 0
# for i,j in grades.items():
#     if i == 'Bob':
#         print(f"{i} is present with marks {j}")
#         flag = 1
#         break
#
# if(flag == 0) :
#     print("Key not found")


#Question-5

# n = int(input("Enter a number :"))
#
# squares = {x:x*x for x in range(1,n+1)}
#
# print(squares)


#Question-6
# d = {'a': 10, 'b': 5, 'c': 15, 'd': 20}
#
# max_value = max(d.values())
# min_value = min(d.values())
#
#
# print(f'Maximum value: {max_value}')
# print(f'Minimum value: {min_value}')

#Question-7
# data = [{'id': 1, 'success': True, 'name': 'Lary'},
#         {'id': 2, 'success': False, 'name': 'Rabi'},
#         {'id': 3, 'success': True, 'name': 'Alex'}]
#
# key = 'success'
# value = True
#
# count = len([d for d in data if d.get(key) == value])
#
#
# print(f"Count of how many dictionaries have {key} as {value}: {count}")

#Quesyion-8


# keys = ['a', 'b', 'c', 'd', 'e', 'c']
# values = [1, 2, 3, 4, 5, 3]
#
# dictionary = {k: v for k, v in zip(keys, values)}
#
# # Print the result
# print(dictionary)






