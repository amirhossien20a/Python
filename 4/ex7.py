studentList = {
    
}

studentCount = int(input("Enter the count of the students : "))

for i in range(studentCount):
    name = input("Enter the student name : ")
    score = int(input("Enter the student score : "))
    studentList[name] = score

def studentListUpdated() :
    updatedList = {}
    FailedStudents = []
    PassedStudents = []
    GoodStudents = []
    ExcellentStudents = []
    for name,score in studentList.items():
        if score < 10 :
            FailedStudents.append(name)
        elif score >= 10 and score <= 14:
            PassedStudents.append(name)
        elif score > 14 and score <= 17 :
            GoodStudents.append(name)
        else :
            ExcellentStudents.append(name)

        updatedList["Failed"] = FailedStudents
        updatedList["Passed"] = PassedStudents
        updatedList["Good"] = GoodStudents
        updatedList["Excellent"] = ExcellentStudents

    return updatedList

print(studentListUpdated())
