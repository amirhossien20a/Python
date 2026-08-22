option = 0
bookList = []
while option != 5:
    print("1-Add book\n2-Show Books\n3-Search book\n4-Remove book\n5-Exit")
    option = int(input("Enter Your Options : "))
    if option == 1 :
        bookName = input("Enter the Book name that you want : ")
        bookList.append(bookName)
        print("Book added succesfuly :)) ")
    elif option == 2 :
        for i in range(len(bookList)):
            print(bookList[i])
    elif option == 3 :
        name = input("Enter the book name that you are looking for : ")
        isAvalible = name in bookList
        if isAvalible == True:
            print("The book that you are looking for is avalible")
        else:
            print("The book that you are looking for is not avalible")
    elif option == 4:
        name = input("Enter the book name that you want to remove : ")
        print(f"{name} is removed from the book list")
        bookList.remove(name)
    elif option == 5 :
        print("Program Closed")
    else :
        print("You have Entered a not correct option")