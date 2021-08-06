while(1):
    print("1. Add name into a file")
    print("2. Display name store in file")
    print("3. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        file = open("ak.txt","w")
        a = input("Enter your name:")
        file.write(a)
    if choice == 2:
        file = open("ak.txt","r")
        y = file.read()
        print("Your name is :")
        print(str(y))  
    if choice == 3:
        break    



