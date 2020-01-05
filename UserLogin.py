def user_login():
    username = 'User12345'
    password = 'Password12345'

    true = bool

    while true:

        EnterUsername = str(input("Enter username : "))

        if EnterUsername == username:

            EnterPassword = str(input("Enter password : "))
            if EnterPassword == password:

                print("Welcome User")

            else:
                print("Wrong password")

        else:
            print("Wrong username")

        x = str(input("Press y/Y to continue : "))

        if x == 'y' or x == 'Y':
            continue

        else:
            break


user_login()
