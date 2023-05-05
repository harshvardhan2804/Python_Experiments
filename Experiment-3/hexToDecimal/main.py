

def hexToInt(a):
    ans = int(a,16)
    return ans

hex_string = input("Enter a hexadecimal code :")

print("Its integer conversion is :" + str(hexToInt(hex_string)))