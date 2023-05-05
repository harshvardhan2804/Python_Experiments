
price1 = int(input("Enter the price of the first good"))
weight1 = int(input("Enter the weight of the first good"))


price2 = int(input("Enter the price of the second good"))
weight2 = int(input("Enter the weight of the second good"))



if(price1/weight1 < price2/weight2):
    print("first one is better")

elif(price1/weight1 > price2/weight2):
    print("second one is better")

else:
    print("both are equally good")