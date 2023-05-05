
def findCommon(str1,str2):
    ans = []
    for i in str1:
        for j in str2:
            if i==j :
                ans.append(i)

    set(ans)
    return ans


string1 = input("Enter string 1 :")
string2 = input("Enter string 2 :")
print(findCommon(string1,string2))