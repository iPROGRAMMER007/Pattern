num = int(input("Enter no of row : "))

for i in range(num):

    for j in range(num - i):
        print("*", end="")

    print()
