
def substringIndex(str,substr):
    ans = str.find(substr)
    return ans

string = input("Enter a string:")
substring = input("Enter the substring :")

res = substringIndex(string,substring)

if res == -1 :
    print("No substring found")
else:
    print(res)

