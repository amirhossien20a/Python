username = "user1234"
password = 12345678
enterUsername = input("Enter the user name")
enterPassword = int(input("Enter the password"))
if(enterUsername == username and password == enterPassword):
    print("Login successful")
elif(enterUsername != username):
    print("Wrong username")
elif(enterUsername == username and enterPassword != password):
    print("Wrong Password")
else:
    print("Login unsuccessful")