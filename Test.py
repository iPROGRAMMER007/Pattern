def calculator():
    print("Calulation starts : from here :) \n")

    true = bool

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    while true:

        print("ADD->1\nSUBTRACT->2\nMULTIPLY->3\nDIVIDE->4\nEnter your choice : ", end="")
        x = int(input())

        if x == 1:

            print(add(10, 10))
        elif x == 2:

            print(sub(10, 10))
        elif x == 3:

            print(mul(10, 10))
        elif x == 4:

            print(div(100, 10))

        else:
            print("Wrong choice ")

        y = int((input("To continue press 5 : ")))
        if y == 5:
            continue
        else:
            print("Thank you")
            break


calculator()
