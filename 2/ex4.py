score = float(input("Enter your score : "))
if(score > 18 and score < 20):
    print("Excellent")
elif(score > 15 and score < 17.99):
    print("Good")
elif(score > 12 and score < 14.99):
    print("Average")
elif(score > 10 and score < 11.99):
    print("Passed")
else:
    print("Failed")