

def divisibility(num):
    if(num%30 == 0):
        print("number is divisible by 5 and 6")

    elif(num % 5 == 0 or num %6 ==0):
        print("Number is divisible by any one of them")


number = int(input("enter a number:"))

divisibility(number)