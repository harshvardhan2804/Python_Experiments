# Calculator

def calc(num1, num2, opr):
    if (opr == '+'):
        return num1 + num2
    elif opr == '-':
        return abs(num1 - num2)
    if opr == '*':
        return num1 * num2
    if opr == '/':
        if num2 == 0:
            return "invalid input"
        else:
            return num1 / num2


for i in range(5):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    opr = input("Enter operation you need to perform:")

    ans = calc(num1, num2, opr)

    print("Answer is " + str(ans))
