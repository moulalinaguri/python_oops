class Faculty:
    def __init__(self, firstName, lastName, email, facultyId, address, mobileNumber, subjectsTeaching, salary, dateJoined):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.facultyId = facultyId
        self.address = address
        self.mobileNumber = mobileNumber
        self.subjectsTeaching = subjectsTeaching
        self.salary = salary
        self.dateJoined = dateJoined

    def getFullName(self):
        print(self.firstName+" "+self.lastName)

    def changeAddress(self, newAddress):
        self.address=newAddress
        print("Address changed successfully")

    def changeNumber(self, newNumber):
        self.mobileNumber = newNumber
        print("Mobile number changed successfully")

    def getSalary(self):
        print("Your Salary is : ", self.salary)


class Student:
    def __init__(self, firstName, lastName, email, studentId, address, mobileNumber, subjectsLearning, GPA, dateJoined):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.studentId = studentId
        self.address = address
        self.mobileNumber = mobileNumber
        self.subjectsLearning = subjectsLearning
        self.GPA = GPA
        self.dateJoined = dateJoined

    def getFullName(self):
        print(self.firstName+" "+self.lastName)

    def changeAddress(self, newAddress):
        self.address=newAddress
        print("Address changed successfully")

    def changeNumber(self, newNumber):
        self.mobileNumber = newNumber
        print("Mobile number changed successfully")

    def getGPA(self):
        print("Your Salary is : ", self.GPA)


