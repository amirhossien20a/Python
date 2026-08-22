balance = 5_000_000
num = int(input("Enter the amount you want : "))
if(num <= 0) :
    print("Invalid")
elif(num > balance):
    print("Insufficient balance")
else:
    newBalance = balance - num
    print("succesul your new balance is " , newBalance)
