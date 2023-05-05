
#Question - 1

# ls =[1,4,5]
#
# ans = 1
# for i in ls :
#     ans *= i
#
# print("product is : " + str(ans))

#Question - 2
#
# ls = ['abc', 'xyz', 'aba', '1221']
#
# count = 0
# for i in ls :
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
#
# print(count)

#Question - 3

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# common_elements = set(list1).intersection(set(list2))
#
# if common_elements:
#     print("The two lists have at least one common element.")
# else:
#     print("The two lists do not have any common elements.")
#


#Question-4

# squares = [i*i for i in range(1,31)]
#
# ans = squares[:5] + squares[-5:]
#
# print(ans)

#Question-5

# def are_circularly_identical(list1, list2):
#     if len(list1) != len(list2):
#         return False
#
#     concatenated_list = list1 + list1
#     if all(elem in concatenated_list[i:i+len(list1)] for i, elem in enumerate(list2)):
#         return True
#
#     return False
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 1, 2]
# list3 = [3, 4, 5, 1, 6]
# print(are_circularly_identical(list1, list2)) # Output: True
# print(are_circularly_identical(list1, list3)) # Output: False

#Question-6

# def to_sorted_array(a,b):
#     temp = [a,b]
#     temp.sort()
#     set(temp)
#     return temp
#
# print(to_sorted_array(3,5))
# print(to_sorted_array(3,6))
# print(to_sorted_array(7,8))
#


# Question-7

# list1 = ["Black", "Red", "Maroon", "Yellow"]
# list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# res ={}
#
# for i,j in zip(list1,list2):
#     res[i]=j
#
# print(res)

# Question-8
# def find_smallest_second_index(tuples):
#     smallest_tuple = tuples[0]
#
#     for t in tuples[1:]:
#         if t[1] < smallest_tuple[1]:
#             smallest_tuple = t
#
#     return smallest_tuple
#
# tuples = [(1, 5), (2, 3), (3, 2), (4, 9), (5, 1)]
# print(find_smallest_second_index(tuples))


# Question-9
# def all_dicts_empty(dicts):
#     return all(not d for d in dicts)
#
# # Example usage:
# list1 = [{}, {}, {}]
# list2 = [{}, {'a': 1}, {}]
# list3 = []
# print(all_dicts_empty(list1)) # Output: True
# print(all_dicts_empty(list2)) # Output: False
# print(all_dicts_empty(list3)) # Output: True
#




