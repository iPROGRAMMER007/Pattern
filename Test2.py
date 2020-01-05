def deposit():

    money = int(input("Enter deposit amount : "))
    print("Amount deposited : ", money)
    initBalance = initBalance + money

    print("Total account balance = ", initBalance)


def withdraw():

    money = int(input("Enter withdraw amount : "))
    print("Amount withdrawl : ", money)
    initBalance = initBalance - money

    print("Total account balance = ", initBalance - money)


def balInquiry():
    initBalance
    print("Total account balance = ", initBalance)


true = bool

while true:

    initBalance = 10000

    def switch(option):

        switcher = {
            1: deposit(),
            2: withdraw(),
            3: balInquiry(),
        }

        return switcher.get(option, "Wrong choice :)")


    op = int(input("1->Deposit\n2->Withdraw\n3->Balance enqury\nEnter your choice : "))
    c = switch(op)
    print(c)

    x = str(input("Press y/Y to continue : "))

    if x == 'y' or x == 'Y':
        continue

    else:
        break
