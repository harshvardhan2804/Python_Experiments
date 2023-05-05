import random


def summ(num1,num2):
    return num1+num2

def isCorrect(sum,num1,num2):
    if sum == summ(num1,num2):
        print("congo you have written it correct")
    else:
        print("oops you have not written it correct")

print("two random numbers are :")

num1 = random.randint(0,100)
num2 = random.randint(0,100)

print(num1)
print(num2)

sum = int(input("Enter sum of two numbers:"))
isCorrect(sum,num1,num2)
