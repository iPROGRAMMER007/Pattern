def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


#true = bool
#while true:

while (1):

    num1 = float(input("Enter first number : "))


    def switch(var):
        num2 = float(input("Enter second number : "))

        switcher = {
            '+': add(num1, num2),
            '-': sub(num1, num2),
            '*': mul(num1, num2),
            '/': div(num1, num2),
        }
        return switcher.get(var, "Option not available :)")


    operator = str(input("Enter operator: "))

    c = switch(operator)
    print(c)

    print("Press y/Y to continue: ", end="")
    x = str(input())
    if x == 'y' or x == 'Y':
        continue

    else:
        break










