#Question - 1

# def calculateCharacters(s):
#     lower=0
#     higher=0
#
#     for i in range(0,len(s)):
#         if s[i]>='a' and s[i]<='z' :
#             lower += 1
#         elif s[i]>='A' and s[i]<='Z' :
#             higher += 1
#
#     return lower,higher
#
#
# str = input("Enter the string :")
# print(calculateCharacters(str))

#Question-2

# str = input("Enter the string :")
#
# temp = str
#
# str[::-1] #to reverse a string
#
# if(temp==str):
#     print("It is pallindrome")
# else:
#     print("It is not a pallindrome")

#Question-3

# import string
#
# def is_pangram(input_string):
#
#     alphabet = set(string.ascii_lowercase)
#
#     # Convert the input string to lowercase and remove all non-alphabetic characters
#     letters = set(filter(lambda char: char.isalpha(), input_string.lower()))
#
#     # Check if the set of letters is equal to the set of all the lowercase letters in the alphabet
#     return letters == alphabet
#
# input_string = "The quick brown fox jumps over the lazy dog"
#
# if is_panagram(input_string):
#     print("The input string is a panagram.")
# else:
#     print("The input string is not a panagram.")

#Question-4
# def count_local_vars():
#
#     a = 1
#     b = "hello"
#     c = [1, 2, 3]
#
#     # locals() is to get a dictionary of local variables
#     local_vars = locals()
#
#     print(local_vars)
#
#     num_local_vars = len(local_vars)
#
#     return num_local_vars
#
# num_locals = count_local_vars()
#
# print("Number of local variables:", num_locals)

