

def stringToList(str):
    li = list(str.split())
    return li

def findRepeated(str):
    temp = stringToList(str)
    flag = False
    ans = ""
    for i in range(0,len(temp)-1):
        for j in range(i+1,len(temp)) :
            if(temp[i]==temp[j]):
                flag = True
                return temp[i]

    if(flag == False):
        print("No repeated character")




string = input("Enter a string : ")

print(findRepeated(string))